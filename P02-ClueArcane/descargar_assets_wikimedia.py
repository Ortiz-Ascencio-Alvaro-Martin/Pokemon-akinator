"""
Descarga assets externos libres para el juego.

Objetivo:
- Obtener imagenes, musica y efectos para el juego.
- Guardar archivos en assets/externos/imagenes y assets/externos/sonidos.
- Generar manifest.json y CREDITOS_ASSETS_EXTERNOS.md.

Fuentes:
- Openverse (principal)
- Wikimedia Commons (respaldo)

Uso:
    python descargar_assets_wikimedia.py
"""

from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse

import requests


COMMONS_API = "https://commons.wikimedia.org/w/api.php"
OPENVERSE_IMAGE_API = "https://api.openverse.org/v1/images/"
OPENVERSE_AUDIO_API = "https://api.openverse.org/v1/audio/"
HEADERS = {
    "User-Agent": "ClueArcaneAssetBot/1.0 (educational project; local downloader)",
}

CARPETA_BASE = Path("assets/externos")
CARPETA_IMAGENES = CARPETA_BASE / "imagenes"
CARPETA_SONIDOS = CARPETA_BASE / "sonidos"
MANIFEST_PATH = CARPETA_BASE / "manifest.json"
CREDITOS_PATH = CARPETA_BASE / "CREDITOS_ASSETS_EXTERNOS.md"

EXT_PERMITIDAS = {
    "imagen": {".jpg", ".jpeg", ".png", ".webp"},
    "audio": {".ogg", ".oga", ".wav", ".mp3"},
}

ASSETS = [
    {
        "slot": "locacion_hextech",
        "tipo": "imagen",
        "consultas": [
            "science laboratory interior",
            "particle accelerator hall",
            "laboratory interior",
        ],
    },
    {
        "slot": "locacion_last_drop",
        "tipo": "imagen",
        "consultas": [
            "pub interior",
            "nightclub interior",
            "tavern interior",
        ],
    },
    {
        "slot": "locacion_consejo",
        "tipo": "imagen",
        "consultas": [
            "parliament chamber interior",
            "council chamber",
            "government hall interior",
        ],
    },
    {
        "slot": "locacion_puente",
        "tipo": "imagen",
        "consultas": [
            "bridge city night",
            "suspension bridge",
            "steel bridge",
        ],
    },
    {
        "slot": "locacion_prision",
        "tipo": "imagen",
        "consultas": [
            "prison corridor",
            "prison gate",
            "fortress prison",
        ],
    },
    {
        "slot": "musica_fondo",
        "tipo": "audio",
        "consultas": [
            'incategory:"Audio files of instrumental music" suspense',
            'incategory:"Audio files of instrumental music" ambient',
            'incategory:"Audio files of instrumental music" drone',
            'incategory:"Audio files of instrumental music" orchestral',
        ],
    },
    {
        "slot": "pista_buena",
        "tipo": "audio",
        "consultas": [
            'incategory:"Audio files of sound effects" bell',
            'incategory:"Audio files" notification sound effect',
            'incategory:"Audio files of instrumental music" victory',
        ],
    },
    {
        "slot": "error",
        "tipo": "audio",
        "consultas": [
            'incategory:"Audio files" alarm sound effect',
            'incategory:"Audio files" error sound effect',
            'incategory:"Audio files of sound effects" click',
        ],
    },
    {
        "slot": "investigacion",
        "tipo": "audio",
        "consultas": [
            'incategory:"Audio files" scanner sound effect',
            'incategory:"Audio files" electronic sound effect',
            'incategory:"Audio files of sound effects" click',
        ],
    },
    {
        "slot": "interrogatorio",
        "tipo": "audio",
        "consultas": [
            'incategory:"Audio files of sound effects" door',
            'incategory:"Audio files of instrumental music" suspense',
            'incategory:"Audio files" ambient drone',
        ],
    },
    {
        "slot": "victoria",
        "tipo": "audio",
        "consultas": [
            'incategory:"Audio files of instrumental music" triumph',
            'incategory:"Audio files of instrumental music" anthem',
            'incategory:"Audio files" fanfare',
        ],
    },
    {
        "slot": "derrota",
        "tipo": "audio",
        "consultas": [
            'incategory:"Audio files" sad sound effect',
            'incategory:"Audio files of instrumental music" lament',
            'incategory:"Audio files" low tone',
        ],
    },
]

FALLBACK_LOCAL_POR_SLOT = {
    "locacion_hextech": Path("assets/imagenes/fondo_piltover.png"),
    "locacion_last_drop": Path("assets/imagenes/fondo_zaun.png"),
    "locacion_consejo": Path("assets/imagenes/fondo_piltover.png"),
    "locacion_puente": Path("assets/imagenes/fondo_piltover.png"),
    "locacion_prision": Path("assets/imagenes/fondo_zaun.png"),
    "musica_fondo": Path("assets/sonidos/musica_fondo.wav"),
    "pista_buena": Path("assets/sonidos/pista_buena.wav"),
    "error": Path("assets/sonidos/error.wav"),
    "investigacion": Path("assets/sonidos/investigacion.wav"),
    "interrogatorio": Path("assets/sonidos/interrogatorio.wav"),
    "victoria": Path("assets/sonidos/victoria.wav"),

    "derrota": Path("assets/sonidos/derrota.wav"),
}


def limpiar_html(texto: str) -> str:
    return re.sub(r"<[^>]+>", "", texto or "").strip()


def limpiar_consulta_openverse(consulta: str) -> str:
    texto = re.sub(r'incategory:"[^"]+"', "", consulta)
    texto = re.sub(r"filetype:\w+", "", texto)
    texto = " ".join(texto.split())
    return texto.strip()


def ext_desde_url_o_mime(url: str, mime: str) -> Optional[str]:
    ext = Path(urlparse(url).path).suffix.lower()
    if ext:
        return ext

    if mime == "audio/ogg":
        return ".ogg"
    if mime == "audio/wav":
        return ".wav"
    if mime == "audio/mpeg":
        return ".mp3"
    if mime == "image/jpeg":
        return ".jpg"
    if mime == "image/png":
        return ".png"
    if mime == "image/webp":
        return ".webp"
    return None


def buscar_en_commons(consulta: str, tipo: str) -> Optional[Dict[str, str]]:
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": consulta,
        "gsrnamespace": 6,
        "gsrlimit": 40,
        "prop": "imageinfo",
        "iiprop": "url|mime|extmetadata",
    }

    try:
        response = requests.get(COMMONS_API, params=params, headers=HEADERS, timeout=15)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return None

    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        imageinfo = (page.get("imageinfo") or [{}])[0]
        url = imageinfo.get("url")
        mime = imageinfo.get("mime", "")
        if not url:
            continue

        ext = ext_desde_url_o_mime(url, mime)
        if not ext or ext not in EXT_PERMITIDAS[tipo]:
            continue

        meta = imageinfo.get("extmetadata", {})
        license_name = limpiar_html(meta.get("LicenseShortName", {}).get("value", ""))
        artist = limpiar_html(meta.get("Artist", {}).get("value", ""))
        credit = limpiar_html(meta.get("Credit", {}).get("value", ""))

        return {
            "title": page.get("title", ""),
            "url": url,
            "mime": mime,
            "extension": ext,
            "description_url": f"https://commons.wikimedia.org/wiki/{page.get('title', '')}",
            "license": license_name or "Verificar en enlace de origen",
            "artist": artist,
            "credit": credit,
        }

    return None


def _licencia_preferida(licencia: str) -> int:
    orden = {
        "cc0": 0,
        "pdm": 1,
        "by": 2,
        "by-sa": 3,
        "cc-by": 4,
        "cc-by-sa": 5,
        "by-nc": 8,
        "by-nd": 9,
        "by-nc-sa": 10,
        "by-nc-nd": 11,
    }
    return orden.get((licencia or "").lower(), 50)


def buscar_en_openverse(consulta: str, tipo: str) -> Optional[Dict[str, str]]:
    endpoint = OPENVERSE_IMAGE_API if tipo == "imagen" else OPENVERSE_AUDIO_API
    consulta_limpia = limpiar_consulta_openverse(consulta)
    if not consulta_limpia:
        return None

    params = {
        "q": consulta_limpia,
        "page_size": 20,
    }

    try:
        response = requests.get(endpoint, params=params, headers=HEADERS, timeout=15)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return None

    candidatos = []
    for item in data.get("results", []):
        if tipo == "imagen":
            # Preferir miniatura para reducir bloqueos por tasa de descarga.
            url = item.get("thumbnail") or item.get("url")
        else:
            url = item.get("url") or item.get("thumbnail")
        if not url:
            continue

        ext = ext_desde_url_o_mime(url, "")
        if not ext or ext not in EXT_PERMITIDAS[tipo]:
            continue

        licencia = (item.get("license") or "").lower()
        candidatos.append(
            {
                "title": item.get("title", ""),
                "url": url,
                "mime": item.get("filetype", ""),
                "extension": ext,
                "description_url": item.get("foreign_landing_url", ""),
                "license": licencia or "desconocida",
                "artist": item.get("creator", ""),
                "credit": item.get("source", "openverse"),
            }
        )

    if not candidatos:
        return None

    candidatos.sort(key=lambda c: _licencia_preferida(c.get("license", "")))
    return candidatos[0]


def descargar_archivo(url: str, destino: Path) -> bool:
    try:
        with requests.get(url, headers=HEADERS, timeout=30, stream=True) as response:
            response.raise_for_status()
            with open(destino, "wb") as output:
                for chunk in response.iter_content(chunk_size=1024 * 32):
                    if chunk:
                        output.write(chunk)
        return True
    except Exception as error:
        print(f"  - descarga fallida: {error}")
        return False


def borrar_anteriores(slot: str, carpeta: Path):
    for existing in carpeta.glob(f"{slot}.*"):
        try:
            existing.unlink()
        except OSError:
            pass


def asegurar_fallback_local(slot: str, tipo: str, registros: List[Dict[str, str]]) -> bool:
    origen = FALLBACK_LOCAL_POR_SLOT.get(slot)
    if origen is None or not origen.exists():
        return False

    carpeta_destino = CARPETA_IMAGENES if tipo == "imagen" else CARPETA_SONIDOS
    destino = carpeta_destino / f"{slot}{origen.suffix.lower()}"
    try:
        shutil.copy2(origen, destino)
        print(f"  ✓ fallback local: {destino.name}")
        registros.append(
            {
                "slot": slot,
                "tipo": tipo,
                "archivo": destino.name,
                "consulta": "fallback_local",
                "source_url": "",
                "description_url": "",
                "license": "interno_proyecto",
                "artist": "generar_recursos.py",
                "credit": "asset local de respaldo",
            }
        )
        return True
    except OSError:
        return False


def guardar_manifest(registros: List[Dict[str, str]]):
    payload = {
        "fuente": "Openverse + Wikimedia Commons",
        "generado_utc": datetime.now(timezone.utc).isoformat(),
        "assets": registros,
    }
    MANIFEST_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def cargar_manifest_previo() -> Dict[str, Dict[str, str]]:
    if not MANIFEST_PATH.exists():
        return {}

    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}

    salida: Dict[str, Dict[str, str]] = {}
    for item in data.get("assets", []):
        slot = item.get("slot")
        if slot and slot not in salida:
            salida[slot] = item
    return salida


def guardar_creditos(registros: List[Dict[str, str]]):
    lineas = [
        "# Creditos de Assets Externos",
        "",
        "Fuente principal: Openverse (respaldo: Wikimedia Commons)",
        "",
        "Este archivo se genera automaticamente con descargar_assets_wikimedia.py.",
        "Verifica la licencia de cada archivo antes de distribuir el proyecto.",
        "",
        "| Slot | Archivo | Licencia | Fuente |",
        "|---|---|---|---|",
    ]

    for r in registros:
        link = r.get("description_url", "")
        lineas.append(
            f"| {r.get('slot', '')} | {r.get('archivo', '')} | {r.get('license', '')} | {link} |"
        )

    CREDITOS_PATH.write_text("\n".join(lineas) + "\n", encoding="utf-8")


def main():
    CARPETA_IMAGENES.mkdir(parents=True, exist_ok=True)
    CARPETA_SONIDOS.mkdir(parents=True, exist_ok=True)

    print("\n=== Descargando assets externos (Openverse + Wikimedia) ===")
    registros: List[Dict[str, str]] = []
    manifest_previo = cargar_manifest_previo()

    for asset in ASSETS:
        slot = asset["slot"]
        tipo = asset["tipo"]
        consultas = asset["consultas"]
        carpeta_destino = CARPETA_IMAGENES if tipo == "imagen" else CARPETA_SONIDOS

        ya_descargados = list(carpeta_destino.glob(f"{slot}.*"))
        if ya_descargados:
            archivo_existente = ya_descargados[0].name
            previo = dict(manifest_previo.get(slot, {}))
            if not previo:
                previo = {
                    "slot": slot,
                    "tipo": tipo,
                    "archivo": archivo_existente,
                    "consulta": "existente_previo",
                    "source_url": "",
                    "description_url": "",
                    "license": "desconocida",
                    "artist": "",
                    "credit": "asset existente",
                }
            else:
                previo["slot"] = slot
                previo["tipo"] = tipo
                previo["archivo"] = archivo_existente

            registros.append(previo)
            print(f"\n[{slot}] ya existe: {archivo_existente} (omitido)")
            continue

        print(f"\n[{slot}] buscando {tipo}...")
        descargado = False

        for consulta in consultas:
            candidato = buscar_en_openverse(consulta, tipo)
            if candidato is None:
                candidato = buscar_en_commons(consulta, tipo)
            if candidato is None:
                continue

            ext = candidato["extension"]
            destino = carpeta_destino / f"{slot}{ext}"

            borrar_anteriores(slot, carpeta_destino)
            if descargar_archivo(candidato["url"], destino):
                print(f"  ✓ descargado: {destino.name}")
                registros.append(
                    {
                        "slot": slot,
                        "tipo": tipo,
                        "archivo": destino.name,
                        "consulta": consulta,
                        "source_url": candidato.get("url", ""),
                        "description_url": candidato.get("description_url", ""),
                        "license": candidato.get("license", ""),
                        "artist": candidato.get("artist", ""),
                        "credit": candidato.get("credit", ""),
                    }
                )
                descargado = True
                break

        if not descargado:
            if not asegurar_fallback_local(slot, tipo, registros):
                print("  - sin resultados compatibles o descargables")

    guardar_manifest(registros)
    guardar_creditos(registros)

    print("\n=== Resumen ===")
    print(f"Assets descargados: {len(registros)}")
    print(f"Manifest: {MANIFEST_PATH}")
    print(f"Creditos: {CREDITOS_PATH}")
    print("\nLa GUI v4 buscara primero en assets/externos/ y luego usara fallback local.")


if __name__ == "__main__":
    main()
