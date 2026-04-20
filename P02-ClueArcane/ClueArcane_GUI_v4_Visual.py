"""
CLUE ARCANE - GUI VISUAL PREMIUM v4.1

Mejoras principales:
- Interfaz reestructurada por secciones claras.
- Tarjetas grandes con hitbox exacta (lo que ves = lo que clickeas).
- Navegacion consistente con boton VOLVER en todas las pantallas internas.
- Pantalla de veredicto mas usable con selectores grandes.
- Feedback visual y sonoro para cada accion.
"""

import math
import random
from enum import Enum
from pathlib import Path
from typing import Dict, Optional, Tuple

import pygame
import requests


# ---------------------------------------------------------------------------
# CONFIGURACION
# ---------------------------------------------------------------------------

PEXELS_API_KEY = "gFLaXlKDHDwz3bMC1r5hKmT2gZhYMF8lJsRgWqEPPyHN0b7kMWZqkPHm"

COLORES = {
    "NEGRO": (15, 15, 20),
    "CARBON": (22, 24, 34),
    "GRIS_OSCURO": (34, 38, 52),
    "GRIS": (62, 69, 88),
    "BLANCO": (240, 245, 252),
    "AZUL_PILTOVER": (40, 122, 188),
    "AZUL_BRILLANTE": (72, 190, 245),
    "NARANJA_ZAUN": (204, 108, 52),
    "NARANJA_BRILLANTE": (255, 156, 82),
    "MAGENTA": (183, 86, 211),
    "CIAN": (78, 214, 220),
    "AMARILLO": (255, 224, 110),
    "ROJO": (210, 78, 78),
    "VERDE": (98, 196, 120),
    "VERDE_OSCURO": (52, 142, 88),
    "DORADO": (231, 188, 90),
}

FUENTES = {
    "TITULO": 56,
    "SUBTITULO": 34,
    "BOTONES": 29,
    "NORMAL": 24,
    "PEQUENA": 20,
}

PERSONAJES = {
    "vi": {
        "nombre": "Vi",
        "color": (220, 102, 194),
        "query": "cyberpunk girl pink hair neon",
        "descripcion": "Vigilante de Zaun",
    },
    "jinx": {
        "nombre": "Jinx",
        "color": (172, 69, 205),
        "query": "crazy girl neon blue eyes",
        "descripcion": "Inventora del caos",
    },
    "jayce": {
        "nombre": "Jayce",
        "color": (84, 170, 222),
        "query": "man warrior blue armor futuristic",
        "descripcion": "Campeon de Piltover",
    },
    "silco": {
        "nombre": "Silco",
        "color": (189, 115, 68),
        "query": "man crime boss dark mysterious",
        "descripcion": "Padrino de Zaun",
    },
    "mel": {
        "nombre": "Mel",
        "color": (222, 196, 102),
        "query": "woman elegant diplomat gold",
        "descripcion": "Diplomatica de Noxus",
    },
}

LOCACIONES = {
    "hextech": {
        "nombre": "Laboratorio Hextech",
        "desc": "Centro de investigacion arcana",
        "color": (94, 149, 220),
        "query": "laboratory futuristic blue neon",
        "rgb_fondo": (38, 62, 122),
    },
    "last_drop": {
        "nombre": "The Last Drop",
        "desc": "Bar clandestino de Zaun",
        "color": (204, 120, 76),
        "query": "bar dark underground neon orange",
        "rgb_fondo": (102, 61, 42),
    },
    "consejo": {
        "nombre": "Consejo de Piltover",
        "desc": "Sede del poder politico",
        "color": (156, 125, 187),
        "query": "council palace elegant fantasy",
        "rgb_fondo": (82, 63, 104),
    },
    "puente": {
        "nombre": "Puente del Progreso",
        "desc": "Frontera entre dos mundos",
        "color": (116, 181, 164),
        "query": "bridge futuristic city landscape",
        "rgb_fondo": (62, 98, 92),
    },
    "prision": {
        "nombre": "Prision Stillwater",
        "desc": "Fortaleza de maxima seguridad",
        "color": (166, 104, 102),
        "query": "prison fortress dark dramatic",
        "rgb_fondo": (98, 64, 63),
    },
}

# Fuentes oficiales/publicas para representar locaciones del juego.
# Se obtienen desde paginas de lugares reales en Wikipedia (Wikimedia).
LOCACIONES_OFICIALES_WIKI = {
    "hextech": ["CERN", "MIT_Media_Lab"],
    "last_drop": ["Public_house", "Nightclub", "Cabaret"],
    "consejo": ["Palace_of_Westminster", "United_States_Capitol"],
    "puente": ["Brooklyn_Bridge", "Tower_Bridge"],
    "prision": ["Alcatraz_Island", "Pentonville_Prison"],
}

LOCACIONES_FALLBACK_LOCAL = {
    "hextech": "fondo_piltover.png",
    "last_drop": "fondo_zaun.png",
    "consejo": "fondo_piltover.png",
    "puente": "fondo_piltover.png",
    "prision": "fondo_zaun.png",
}

CARPETA_EXTERNOS_IMAGENES = Path("assets/externos/imagenes")
CARPETA_EXTERNOS_SONIDOS = Path("assets/externos/sonidos")

ARMAS = {
    "guanteletes": "Guanteletes Atlas",
    "lanzacohetes": "Lanzacohetes Espinas",
    "shimmer": "Jeringa de Shimmer",
    "hextech": "Nucleo Hextech",
    "bomba": "Bomba de Fuego",
}


class Pantalla(Enum):
    INICIO = 1
    MENU = 2
    INVESTIGAR = 3
    INTERROGAR = 4
    PISTAS = 5
    VEREDICTO = 6
    FINAL = 7


def aclarar(color: Tuple[int, int, int], delta: int = 22) -> Tuple[int, int, int]:
    return tuple(min(255, c + delta) for c in color)


# ---------------------------------------------------------------------------
# IMAGENES
# ---------------------------------------------------------------------------

class GestorImagenes:
    """Descarga imagenes desde Pexels y las guarda en cache local."""

    def __init__(self, cache_dir: str = "assets/cache_imagenes"):
        self.api_key = PEXELS_API_KEY
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.memoria: Dict[str, pygame.Surface] = {}
        self.online = self._verificar_conexion()

    def _verificar_conexion(self) -> bool:
        try:
            requests.head("https://api.pexels.com", timeout=3)
            print("✓ Conexion con Pexels API")
            return True
        except Exception:
            print("⚠ Sin conexion. Se usaran placeholders visuales")
            return False

    def _cache_path(self, cache_key: str) -> Path:
        return self.cache_dir / f"{cache_key}.jpg"

    def _cargar_desde_cache(self, cache_key: str, ancho: int, alto: int) -> Optional[pygame.Surface]:
        if cache_key in self.memoria:
            return self.memoria[cache_key]

        cache_path = self._cache_path(cache_key)
        if cache_path.exists():
            try:
                imagen = pygame.image.load(str(cache_path))
                imagen = pygame.transform.smoothscale(imagen, (ancho, alto))
                self.memoria[cache_key] = imagen
                return imagen
            except Exception:
                return None
        return None

    def _descargar_y_guardar(self, url: str, cache_key: str, ancho: int, alto: int) -> Optional[pygame.Surface]:
        try:
            respuesta = requests.get(url, timeout=6)
            if respuesta.status_code != 200:
                return None

            cache_path = self._cache_path(cache_key)
            with open(cache_path, "wb") as archivo:
                archivo.write(respuesta.content)

            imagen = pygame.image.load(str(cache_path))
            imagen = pygame.transform.smoothscale(imagen, (ancho, alto))
            self.memoria[cache_key] = imagen
            return imagen
        except Exception:
            return None

    def _crear_placeholder(self, ancho: int, alto: int) -> pygame.Surface:
        superficie = pygame.Surface((ancho, alto))

        # Fondo degradado oscuro para evitar el efecto de "rejilla vacia".
        for y in range(alto):
            t = y / max(1, alto - 1)
            r = int(22 + 12 * (1 - t))
            g = int(28 + 20 * (1 - t))
            b = int(42 + 35 * (1 - t))
            pygame.draw.line(superficie, (r, g, b), (0, y), (ancho, y))

        # Brillo ambiental.
        brillo = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        pygame.draw.ellipse(
            brillo,
            (72, 190, 245, 60),
            (int(ancho * 0.55), int(alto * 0.08), int(ancho * 0.42), int(alto * 0.66)),
        )
        pygame.draw.ellipse(
            brillo,
            (255, 156, 82, 46),
            (int(ancho * 0.02), int(alto * 0.30), int(ancho * 0.42), int(alto * 0.56)),
        )
        superficie.blit(brillo, (0, 0))

        # Siluetas urbanas simples.
        for i in range(0, ancho + 20, max(18, ancho // 16)):
            altura = int(alto * (0.25 + ((i * 37) % 40) / 100))
            rect = pygame.Rect(i, alto - altura, max(14, ancho // 26), altura)
            pygame.draw.rect(superficie, (14, 16, 26), rect)

        # Viñeta suave.
        v = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        pygame.draw.rect(v, (0, 0, 0, 70), (0, 0, ancho, alto), border_radius=18)
        pygame.draw.rect(v, (0, 0, 0, 0), (8, 8, ancho - 16, alto - 16), border_radius=14)
        superficie.blit(v, (0, 0))
        return superficie

    def descargar_imagen_wikipedia(
        self,
        titulo_pagina: str,
        cache_key_base: str,
        ancho: int,
        alto: int,
    ) -> Optional[pygame.Surface]:
        """Obtiene imagen de una pagina de Wikipedia (lugar oficial/publico)."""
        cache_key = f"wiki_{cache_key_base}_{ancho}_{alto}"

        imagen_cache = self._cargar_desde_cache(cache_key, ancho, alto)
        if imagen_cache is not None:
            return imagen_cache

        if not self.online:
            return None

        try:
            # Ruta principal: API Summary de Wikipedia (mas fiable para thumbnails).
            summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{titulo_pagina}"
            summary = requests.get(summary_url, timeout=6)
            if summary.status_code == 200:
                source = summary.json().get("thumbnail", {}).get("source")
                if source:
                    imagen = self._descargar_y_guardar(source, cache_key, ancho, alto)
                    if imagen is not None:
                        print(f"  ✓ Wikipedia: {titulo_pagina}")
                        return imagen

            # Respaldo: API query legacy por si el endpoint summary no entrega miniatura.
            params = {
                "action": "query",
                "format": "json",
                "prop": "pageimages",
                "piprop": "thumbnail",
                "pithumbsize": max(ancho, alto) * 4,
                "titles": titulo_pagina,
            }
            respuesta = requests.get("https://en.wikipedia.org/w/api.php", params=params, timeout=6)
            if respuesta.status_code != 200:
                return None

            pages = respuesta.json().get("query", {}).get("pages", {})
            for pagina in pages.values():
                source = pagina.get("thumbnail", {}).get("source")
                if source:
                    imagen = self._descargar_y_guardar(source, cache_key, ancho, alto)
                    if imagen is not None:
                        print(f"  ✓ Wikipedia: {titulo_pagina}")
                        return imagen
        except Exception as error:
            print(f"  ⚠ Wikipedia '{titulo_pagina}': {error}")

        return None

    def descargar_imagen(self, query: str, ancho: int, alto: int) -> pygame.Surface:
        cache_key = f"pexels_{query}_{ancho}_{alto}".replace(" ", "_")

        imagen_cache = self._cargar_desde_cache(cache_key, ancho, alto)
        if imagen_cache is not None:
            return imagen_cache

        if not self.online:
            imagen = self._crear_placeholder(ancho, alto)
            self.memoria[cache_key] = imagen
            return imagen

        try:
            headers = {"Authorization": self.api_key}
            params = {"query": query, "per_page": 1, "size": "small"}
            respuesta = requests.get(
                "https://api.pexels.com/v1/search",
                headers=headers,
                params=params,
                timeout=6,
            )

            if respuesta.status_code == 200:
                datos = respuesta.json()
                fotos = datos.get("photos", [])
                if fotos:
                    img_url = fotos[0]["src"]["medium"]
                    imagen = self._descargar_y_guardar(img_url, cache_key, ancho, alto)
                    if imagen is not None:
                        print(f"  ✓ {query}")
                        return imagen
        except Exception as error:
            print(f"  ⚠ Error con '{query}': {error}")

        imagen = self._crear_placeholder(ancho, alto)
        self.memoria[cache_key] = imagen
        return imagen


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

class Boton:
    def __init__(
        self,
        x: int,
        y: int,
        ancho: int,
        alto: int,
        texto: str,
        color_normal: Tuple[int, int, int],
        color_hover: Tuple[int, int, int],
    ):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.habilitado = True

    def contiene(self, pos: Tuple[int, int]) -> bool:
        return self.habilitado and self.rect.collidepoint(pos)

    def dibujar(
        self,
        superficie: pygame.Surface,
        fuente: pygame.font.Font,
        mouse_pos: Tuple[int, int],
        texto_color: Tuple[int, int, int] = COLORES["BLANCO"],
    ):
        hover = self.habilitado and self.rect.collidepoint(mouse_pos)
        color = self.color_hover if hover else self.color_normal
        if not self.habilitado:
            color = COLORES["GRIS"]

        sombra = self.rect.move(0, 4)
        pygame.draw.rect(superficie, (0, 0, 0, 90), sombra, border_radius=14)
        pygame.draw.rect(superficie, color, self.rect, border_radius=14)
        pygame.draw.rect(superficie, COLORES["BLANCO"], self.rect, 2, border_radius=14)

        if hover:
            brillo = self.rect.inflate(8, 8)
            pygame.draw.rect(superficie, color, brillo, 2, border_radius=18)

        texto = fuente.render(self.texto, True, texto_color)
        superficie.blit(texto, texto.get_rect(center=self.rect.center))


class ClueArcaneVisual:
    def __init__(self):
        pygame.init()

        self.ancho, self.alto = 1500, 920
        self.margen = 32
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("CLUE ARCANE - Visual Premium")
        self.reloj = pygame.time.Clock()
        self.corriendo = True

        self.audio_disponible = True
        try:
            pygame.mixer.init()
        except pygame.error:
            self.audio_disponible = False
            print("⚠ Audio no disponible en este entorno")

        self.fuentes = {
            "titulo": pygame.font.SysFont("georgia", FUENTES["TITULO"], bold=True),
            "subtitulo": pygame.font.SysFont("cambria", FUENTES["SUBTITULO"], bold=True),
            "botones": pygame.font.SysFont("segoeui", FUENTES["BOTONES"], bold=True),
            "normal": pygame.font.SysFont("segoeui", FUENTES["NORMAL"]),
            "pequena": pygame.font.SysFont("segoeui", FUENTES["PEQUENA"]),
        }

        print("\n📥 Cargando recursos visuales...")
        self.gestor_imagenes = GestorImagenes()
        self.imagenes_personajes: Dict[str, pygame.Surface] = {}
        self.imagenes_locaciones: Dict[str, pygame.Surface] = {}
        self._cargar_imagenes()

        self.sonidos: Dict[str, pygame.mixer.Sound] = {}
        self._cargar_sonidos()

        # Estado de juego
        self.pantalla_actual = Pantalla.INICIO
        self.culpable: Optional[str] = None
        self.locacion_crimen: Optional[str] = None
        self.arma_crimen: Optional[str] = None

        self.locaciones_investigadas = set()
        self.personajes_interrogados = set()
        self.pistas_descubiertas = []
        self.pista_ids = set()
        self.tema_actual = (42, 64, 108)

        self.indices_veredicto = {"personaje": 0, "locacion": 0, "arma": 0}

        self.resultado_correcto = False
        self.resultado_texto = ""

        self.toast_texto = ""
        self.toast_color = COLORES["AMARILLO"]
        self.toast_frames = 0

        self._fondos_cache: Dict[Tuple[int, int, int], pygame.Surface] = {}
        self._frame_anim = 0

        self._crear_botones()
        print("✓ Interfaz lista\n")

    # ------------------------------------------------------------------
    # CARGA DE RECURSOS
    # ------------------------------------------------------------------

    def _cargar_imagen_local(self, ruta: Path, ancho: int, alto: int) -> Optional[pygame.Surface]:
        if not ruta.exists():
            return None
        try:
            imagen = pygame.image.load(str(ruta))
            return pygame.transform.smoothscale(imagen, (ancho, alto))
        except pygame.error:
            return None

    def _buscar_imagen_por_base(self, base_name: str, ancho: int, alto: int) -> Optional[pygame.Surface]:
        extensiones = [".png", ".jpg", ".jpeg", ".webp"]
        for ext in extensiones:
            ruta = CARPETA_EXTERNOS_IMAGENES / f"{base_name}{ext}"
            imagen = self._cargar_imagen_local(ruta, ancho, alto)
            if imagen is not None:
                print(f"  ✓ Externo: {ruta.name}")
                return imagen
        return None

    def _buscar_audio_por_base(self, base_name: str) -> Optional[Path]:
        extensiones = [".ogg", ".wav", ".oga", ".mp3"]
        carpetas = [CARPETA_EXTERNOS_SONIDOS, Path("assets/sonidos")]

        for carpeta in carpetas:
            for ext in extensiones:
                ruta = carpeta / f"{base_name}{ext}"
                if ruta.exists():
                    return ruta
        return None

    def _cargar_imagenes(self):
        print("\n👥 Personajes")
        for key, data in PERSONAJES.items():
            imagen_personaje = self._buscar_imagen_por_base(f"personaje_{key}", 210, 130)
            if imagen_personaje is None:
                imagen_personaje = self.gestor_imagenes.descargar_imagen(data["query"], 210, 130)
            self.imagenes_personajes[key] = imagen_personaje

        print("\n🏙 Locaciones")
        for key, data in LOCACIONES.items():
            imagen_oficial = self._buscar_imagen_por_base(f"locacion_{key}", 280, 130)
            if imagen_oficial is not None:
                self.imagenes_locaciones[key] = imagen_oficial
                continue

            imagen_oficial = None
            candidatos = LOCACIONES_OFICIALES_WIKI.get(key, [])
            for titulo in candidatos:
                imagen_oficial = self.gestor_imagenes.descargar_imagen_wikipedia(
                    titulo, f"{key}_{titulo}", 280, 130
                )
                if imagen_oficial is not None:
                    break

            if imagen_oficial is None:
                local_name = LOCACIONES_FALLBACK_LOCAL.get(key)
                if local_name:
                    ruta_local = Path("assets/imagenes") / local_name
                    imagen_oficial = self._cargar_imagen_local(ruta_local, 280, 130)
                    if imagen_oficial is not None:
                        print(f"  ✓ Local: {local_name}")

            if imagen_oficial is None:
                imagen_oficial = self.gestor_imagenes.descargar_imagen(data["query"], 280, 130)

            self.imagenes_locaciones[key] = imagen_oficial

    def _cargar_sonidos(self):
        if not self.audio_disponible:
            return

        # Música de fondo: prioriza assets externos y usa pygame.mixer.music para streaming.
        ruta_musica = self._buscar_audio_por_base("musica_fondo")
        if ruta_musica is not None:
            try:
                pygame.mixer.music.load(str(ruta_musica))
                pygame.mixer.music.set_volume(0.52)
                pygame.mixer.music.play(-1, fade_ms=1200)
                print(f"  ✓ Musica cargada: {ruta_musica.name}")
            except pygame.error:
                pass

        # Efectos de sonido.
        slots_sfx = {
            "pista": "pista_buena",
            "error": "error",
            "investigar": "investigacion",
            "interrogar": "interrogatorio",
            "victoria": "victoria",
            "derrota": "derrota",
        }

        for nombre, base_archivo in slots_sfx.items():
            ruta = self._buscar_audio_por_base(base_archivo)
            if ruta is None:
                continue
            try:
                self.sonidos[nombre] = pygame.mixer.Sound(str(ruta))
                print(f"  ✓ SFX cargado: {ruta.name}")
            except pygame.error:
                pass

        volumenes = {
            "pista": 0.80,
            "error": 0.55,
            "investigar": 0.65,
            "interrogar": 0.62,
            "victoria": 0.82,
            "derrota": 0.72,
        }
        for nombre, volumen in volumenes.items():
            if nombre in self.sonidos:
                self.sonidos[nombre].set_volume(volumen)

    def _reproducir(self, nombre: str):
        if nombre in self.sonidos:
            self.sonidos[nombre].play()

    # ------------------------------------------------------------------
    # ESTADO Y LOGICA
    # ------------------------------------------------------------------

    def _crear_botones(self):
        centro_x = self.ancho // 2

        self.botones_inicio = {
            "iniciar": Boton(
                centro_x - 200,
                500,
                400,
                72,
                "INICIAR INVESTIGACION",
                COLORES["AZUL_PILTOVER"],
                COLORES["AZUL_BRILLANTE"],
            ),
            "salir": Boton(
                centro_x - 200,
                590,
                400,
                66,
                "SALIR",
                COLORES["ROJO"],
                aclarar(COLORES["ROJO"], 25),
            ),
        }

        self.botones_menu = {
            "investigar": Boton(
                66,
                262,
                670,
                152,
                "🔍 INVESTIGAR LUGARES",
                COLORES["AZUL_PILTOVER"],
                COLORES["AZUL_BRILLANTE"],
            ),
            "interrogar": Boton(
                764,
                262,
                670,
                152,
                "🎭 INTERROGAR PERSONAJES",
                COLORES["NARANJA_ZAUN"],
                COLORES["NARANJA_BRILLANTE"],
            ),
            "pistas": Boton(
                66,
                438,
                670,
                152,
                "💡 REVISAR PISTAS",
                COLORES["MAGENTA"],
                aclarar(COLORES["MAGENTA"], 18),
            ),
            "veredicto": Boton(
                764,
                438,
                670,
                152,
                "⚖ EMITIR VEREDICTO",
                COLORES["VERDE_OSCURO"],
                COLORES["VERDE"],
            ),
        }

        self.boton_volver = Boton(
            self.ancho - 248,
            30,
            210,
            52,
            "VOLVER",
            COLORES["GRIS"],
            aclarar(COLORES["GRIS"], 18),
        )

        self.botones_final = {
            "nuevo": Boton(
                self.ancho // 2 - 260,
                700,
                250,
                66,
                "JUGAR DE NUEVO",
                COLORES["AZUL_PILTOVER"],
                COLORES["AZUL_BRILLANTE"],
            ),
            "salir": Boton(
                self.ancho // 2 + 10,
                700,
                250,
                66,
                "SALIR",
                COLORES["ROJO"],
                aclarar(COLORES["ROJO"], 25),
            ),
        }

    def _mostrar_toast(self, texto: str, color: Tuple[int, int, int] = COLORES["AMARILLO"]):
        self.toast_texto = texto
        self.toast_color = color
        self.toast_frames = 180

    def _agregar_pista(self, pista_id: str, texto: str, tipo: str, correcta: bool):
        if pista_id in self.pista_ids:
            return
        self.pista_ids.add(pista_id)
        self.pistas_descubiertas.append(
            {
                "texto": texto,
                "tipo": tipo,
                "correcta": correcta,
            }
        )

    def _iniciar_juego(self):
        self.culpable = random.choice(list(PERSONAJES.keys()))
        self.locacion_crimen = random.choice(list(LOCACIONES.keys()))
        self.arma_crimen = random.choice(list(ARMAS.keys()))

        self.locaciones_investigadas.clear()
        self.personajes_interrogados.clear()
        self.pistas_descubiertas.clear()
        self.pista_ids.clear()

        self.tema_actual = (42, 64, 108)
        self.indices_veredicto = {"personaje": 0, "locacion": 0, "arma": 0}

        self.resultado_correcto = False
        self.resultado_texto = ""

        self._mostrar_toast("Caso iniciado. Reune evidencia antes del veredicto.", COLORES["CIAN"])
        self._reproducir("investigar")
        self.pantalla_actual = Pantalla.MENU

    def _investigar_locacion(self, key: str):
        if key in self.locaciones_investigadas:
            self._mostrar_toast("Esa locacion ya fue investigada.", COLORES["AMARILLO"])
            return

        self.locaciones_investigadas.add(key)
        self.tema_actual = LOCACIONES[key]["rgb_fondo"]

        if key == self.locacion_crimen:
            texto = f"Coincidencia fuerte: el crimen apunta a {LOCACIONES[key]['nombre']}."
            self._agregar_pista(f"loc_true_{key}", texto, "locacion", True)
            self._reproducir("pista")
            self._mostrar_toast("Pista fuerte obtenida en la escena.", COLORES["VERDE"])
        else:
            texto = f"{LOCACIONES[key]['nombre']} no presenta evidencia concluyente."
            self._agregar_pista(f"loc_false_{key}", texto, "locacion", False)
            self._reproducir("error")
            self._mostrar_toast("Locacion descartada por ahora.", COLORES["AMARILLO"])

        if len(self.locaciones_investigadas) >= 2:
            arma_texto = f"Forense sugiere uso de: {ARMAS[self.arma_crimen]}."
            self._agregar_pista("arma_forense", arma_texto, "arma", True)

        self.pantalla_actual = Pantalla.MENU

    def _interrogar_personaje(self, key: str):
        if key in self.personajes_interrogados:
            self._mostrar_toast("Ese personaje ya fue interrogado.", COLORES["AMARILLO"])
            return

        self.personajes_interrogados.add(key)

        if key == self.culpable:
            texto = f"{PERSONAJES[key]['nombre']} se contradice en su coartada."
            self._agregar_pista(f"pers_true_{key}", texto, "personaje", True)
            self._reproducir("pista")
            self._mostrar_toast("Interrogatorio revelador.", COLORES["VERDE"])
        else:
            texto = f"{PERSONAJES[key]['nombre']} mantiene una coartada consistente."
            self._agregar_pista(f"pers_false_{key}", texto, "personaje", False)
            self._reproducir("interrogar")
            self._mostrar_toast("Nada concluyente en esta declaracion.", COLORES["AMARILLO"])

        self.pantalla_actual = Pantalla.MENU

    def _lista_por_tipo(self, tipo: str):
        if tipo == "personaje":
            return list(PERSONAJES.keys())
        if tipo == "locacion":
            return list(LOCACIONES.keys())
        return list(ARMAS.keys())

    def _actual_seleccion(self, tipo: str) -> str:
        lista = self._lista_por_tipo(tipo)
        return lista[self.indices_veredicto[tipo] % len(lista)]

    def _mover_selector(self, tipo: str, paso: int):
        lista = self._lista_por_tipo(tipo)
        self.indices_veredicto[tipo] = (self.indices_veredicto[tipo] + paso) % len(lista)

    def _emitir_veredicto(self):
        sel_personaje = self._actual_seleccion("personaje")
        sel_locacion = self._actual_seleccion("locacion")
        sel_arma = self._actual_seleccion("arma")

        self.resultado_correcto = (
            sel_personaje == self.culpable
            and sel_locacion == self.locacion_crimen
            and sel_arma == self.arma_crimen
        )

        if self.resultado_correcto:
            self.resultado_texto = "Caso resuelto. Tu investigacion fue impecable."
            self._reproducir("victoria")
        else:
            self.resultado_texto = "Veredicto incorrecto. El crimen sigue bajo analisis."
            self._reproducir("derrota")

        self.pantalla_actual = Pantalla.FINAL

    # ------------------------------------------------------------------
    # LAYOUT REUTILIZABLE
    # ------------------------------------------------------------------

    def _rects_locaciones(self) -> Dict[str, pygame.Rect]:
        rects = {}
        card_w = (self.ancho - self.margen * 3) // 2
        card_h = 146
        inicio_y = 136
        gap_y = 16
        for idx, key in enumerate(LOCACIONES.keys()):
            fila = idx // 2
            col = idx % 2
            x = self.margen + col * (card_w + self.margen)
            y = inicio_y + fila * (card_h + gap_y)
            rects[key] = pygame.Rect(x, y, card_w, card_h)
        return rects

    def _rects_personajes(self) -> Dict[str, pygame.Rect]:
        rects = {}
        card_w = (self.ancho - self.margen * 3) // 2
        card_h = 146
        inicio_y = 136
        gap_y = 16
        for idx, key in enumerate(PERSONAJES.keys()):
            fila = idx // 2
            col = idx % 2
            x = self.margen + col * (card_w + self.margen)
            y = inicio_y + fila * (card_h + gap_y)
            rects[key] = pygame.Rect(x, y, card_w, card_h)
        return rects

    def _rects_veredicto(self) -> Dict[str, pygame.Rect]:
        rects: Dict[str, pygame.Rect] = {}
        tipos = ["personaje", "locacion", "arma"]
        for i, tipo in enumerate(tipos):
            y = 152 + i * 210
            rects[f"{tipo}_prev"] = pygame.Rect(94, y + 36, 74, 74)
            rects[f"{tipo}_next"] = pygame.Rect(self.ancho - 168, y + 36, 74, 74)
            rects[f"{tipo}_valor"] = pygame.Rect(196, y, self.ancho - 392, 146)

        rects["confirmar"] = pygame.Rect(self.ancho // 2 - 230, 804, 460, 68)
        return rects

    # ------------------------------------------------------------------
    # RENDER
    # ------------------------------------------------------------------

    def _construir_fondo_cinematico(self, base: Tuple[int, int, int]) -> pygame.Surface:
        superficie = pygame.Surface((self.ancho, self.alto))

        # Gradiente base profundo.
        for y in range(self.alto):
            t = y / self.alto
            r = int(base[0] * (1 - t) + 14 * t)
            g = int(base[1] * (1 - t) + 12 * t)
            b = int(base[2] * (1 - t) + 22 * t)
            pygame.draw.line(superficie, (r, g, b), (0, y), (self.ancho, y))

        # Capa horizontal hibrida Arcane (Piltover azul + Zaun naranja).
        mezcla = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        for x in range(self.ancho):
            tx = x / max(1, self.ancho - 1)
            azul = COLORES["AZUL_BRILLANTE"]
            naranja = COLORES["NARANJA_BRILLANTE"]
            mr = int(azul[0] * (1 - tx) + naranja[0] * tx)
            mg = int(azul[1] * (1 - tx) + naranja[1] * tx)
            mb = int(azul[2] * (1 - tx) + naranja[2] * tx)
            alpha = int(34 + 30 * (1 - abs(tx - 0.5) * 2))
            pygame.draw.line(mezcla, (mr, mg, mb, alpha), (x, 0), (x, self.alto))
        superficie.blit(mezcla, (0, 0))

        # Brillos principales tipo neón (Piltover/Zaun).
        brillo = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        acento_a = aclarar(base, 48)
        acento_b = COLORES["NARANJA_BRILLANTE"]
        pygame.draw.ellipse(
            brillo,
            (acento_a[0], acento_a[1], acento_a[2], 78),
            (int(self.ancho * 0.54), int(self.alto * 0.06), 700, 390),
        )
        pygame.draw.ellipse(
            brillo,
            (acento_b[0], acento_b[1], acento_b[2], 58),
            (int(self.ancho * 0.02), int(self.alto * 0.24), 620, 330),
        )
        superficie.blit(brillo, (0, 0))

        # Skyline estilizado.
        base_y = int(self.alto * 0.74)
        for i in range(0, self.ancho + 80, 64):
            altura = int(80 + ((i * 41) % 190))
            edificio = pygame.Rect(i, base_y - altura, 54, altura)
            pygame.draw.rect(superficie, (12, 14, 25), edificio)

            # Ventanas suaves.
            if (i // 64) % 2 == 0:
                for wy in range(edificio.y + 10, edificio.bottom - 10, 16):
                    pygame.draw.rect(superficie, (180, 190, 120), (i + 8, wy, 6, 4))

        # Rayos de luz verticales para dramatismo alto.
        rayos = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        for x in range(120, self.ancho, 220):
            pygame.draw.rect(rayos, (72, 190, 245, 18), (x, 0, 3, self.alto))
        for x in range(220, self.ancho, 280):
            pygame.draw.rect(rayos, (255, 156, 82, 16), (x, 0, 2, self.alto))
        superficie.blit(rayos, (0, 0))

        # Vigneta para enfoque central.
        vigneta = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        pygame.draw.rect(vigneta, (0, 0, 0, 95), (0, 0, self.ancho, self.alto), border_radius=28)
        pygame.draw.rect(
            vigneta,
            (0, 0, 0, 0),
            (20, 20, self.ancho - 40, self.alto - 40),
            border_radius=24,
        )
        superficie.blit(vigneta, (0, 0))

        return superficie

    def _dibujar_fondo(self, base: Tuple[int, int, int]):
        key = tuple(base)
        if key not in self._fondos_cache:
            self._fondos_cache[key] = self._construir_fondo_cinematico(base)

        self.pantalla.blit(self._fondos_cache[key], (0, 0))

        # Neblina animada para que el fondo no se sienta estático.
        self._frame_anim += 1
        t = self._frame_anim * 0.013
        neblina = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        for i in range(3):
            cx = int((math.sin(t + i * 1.4) * 0.5 + 0.5) * self.ancho)
            cy = int(self.alto * (0.24 + i * 0.2))
            rx = 280 + i * 110
            ry = 86 + i * 22
            color = (72, 190, 245, 18) if i % 2 == 0 else (255, 156, 82, 14)
            pygame.draw.ellipse(neblina, color, (cx - rx, cy - ry, rx * 2, ry * 2))
        self.pantalla.blit(neblina, (0, 0))

    def _dibujar_header(
        self,
        titulo: str,
        subtitulo: str = "",
        color: Tuple[int, int, int] = COLORES["AZUL_BRILLANTE"],
        mostrar_volver: bool = False,
    ):
        panel = pygame.Surface((self.ancho, 104), pygame.SRCALPHA)
        panel.fill((8, 10, 18, 170))
        self.pantalla.blit(panel, (0, 0))

        pulso = 0.75 + 0.25 * math.sin(self._frame_anim * 0.09)
        color_linea = (
            min(255, int(color[0] * pulso + 18)),
            min(255, int(color[1] * pulso + 18)),
            min(255, int(color[2] * pulso + 18)),
        )
        pygame.draw.line(self.pantalla, color_linea, (24, 98), (self.ancho - 24, 98), 3)

        # Destello desplazándose por la línea del header.
        spark_x = 24 + int((self._frame_anim * 7) % (self.ancho - 48))
        pygame.draw.circle(self.pantalla, COLORES["BLANCO"], (spark_x, 98), 4)

        t = self.fuentes["titulo"].render(titulo, True, color)
        self.pantalla.blit(t, (30, 14))

        if subtitulo:
            s = self.fuentes["pequena"].render(subtitulo, True, COLORES["BLANCO"])
            self.pantalla.blit(s, (32, 68))

        if mostrar_volver:
            self.boton_volver.dibujar(self.pantalla, self.fuentes["botones"], pygame.mouse.get_pos())

    def _dibujar_toast(self):
        if self.toast_frames <= 0:
            return

        self.toast_frames -= 1
        ancho = min(920, max(300, len(self.toast_texto) * 11))
        rect = pygame.Rect((self.ancho - ancho) // 2, self.alto - 70, ancho, 42)
        pygame.draw.rect(self.pantalla, COLORES["CARBON"], rect, border_radius=10)
        pygame.draw.rect(self.pantalla, self.toast_color, rect, 2, border_radius=10)
        txt = self.fuentes["pequena"].render(self.toast_texto, True, COLORES["BLANCO"])
        self.pantalla.blit(txt, txt.get_rect(center=rect.center))

    def _dibujar_inicio(self):
        self._dibujar_fondo((32, 58, 110))
        self._dibujar_header(
            "CLUE ARCANE",
            "Investigacion visual en Piltover y Zaun",
            COLORES["AZUL_BRILLANTE"],
        )

        mouse = pygame.mouse.get_pos()

        texto_1 = self.fuentes["subtitulo"].render("El Misterio de Piltover y Zaun", True, COLORES["NARANJA_BRILLANTE"])
        self.pantalla.blit(texto_1, (82, 186))

        info = [
            "• Investiga locaciones con tematica visual propia",
            "• Interroga personajes y analiza contradicciones",
            "• Emite un veredicto con personaje, lugar y arma",
        ]
        y = 258
        for linea in info:
            t = self.fuentes["normal"].render(linea, True, COLORES["BLANCO"])
            self.pantalla.blit(t, (90, y))
            y += 42

        # Mosaico visual
        preview_rect = pygame.Rect(860, 150, 580, 350)
        pygame.draw.rect(self.pantalla, COLORES["GRIS_OSCURO"], preview_rect, border_radius=16)
        pygame.draw.rect(self.pantalla, COLORES["CIAN"], preview_rect, 2, border_radius=16)

        loc_keys = list(LOCACIONES.keys())
        if loc_keys:
            img = self.imagenes_locaciones[loc_keys[0]]
            self.pantalla.blit(img, (876, 168))
        if len(loc_keys) > 1:
            img2 = self.imagenes_locaciones[loc_keys[1]]
            self.pantalla.blit(img2, (1160, 168))

        if loc_keys:
            nombre = self.fuentes["pequena"].render("Ambientes reales de investigacion", True, COLORES["BLANCO"])
            self.pantalla.blit(nombre, (880, 324))

        self.botones_inicio["iniciar"].dibujar(self.pantalla, self.fuentes["botones"], mouse)
        self.botones_inicio["salir"].dibujar(self.pantalla, self.fuentes["botones"], mouse)

    def _dibujar_menu(self):
        self._dibujar_fondo(self.tema_actual)
        self._dibujar_header(
            "CENTRO DE INVESTIGACION",
            "Selecciona una accion. Las tarjetas tienen hitbox amplia y precisa.",
            COLORES["AZUL_BRILLANTE"],
        )

        # Estado rapido
        panel = pygame.Rect(66, 130, 1368, 106)
        pygame.draw.rect(self.pantalla, COLORES["CARBON"], panel, border_radius=12)
        pygame.draw.rect(self.pantalla, COLORES["DORADO"], panel, 2, border_radius=12)

        stats = [
            f"Locaciones investigadas: {len(self.locaciones_investigadas)}/5",
            f"Personajes interrogados: {len(self.personajes_interrogados)}/5",
            f"Pistas disponibles: {len(self.pistas_descubiertas)}",
        ]
        x = 100
        for texto in stats:
            t = self.fuentes["normal"].render(texto, True, COLORES["BLANCO"])
            self.pantalla.blit(t, (x, 170))
            x += 430

        mouse = pygame.mouse.get_pos()
        descripciones = {
            "investigar": "Explora cada lugar y busca evidencia.",
            "interrogar": "Contrasta coartadas y detecta contradicciones.",
            "pistas": "Revisa toda la informacion reunida.",
            "veredicto": "Acusa personaje, lugar y arma.",
        }

        for key, boton in self.botones_menu.items():
            boton.dibujar(self.pantalla, self.fuentes["botones"], mouse)
            sub = self.fuentes["pequena"].render(descripciones[key], True, COLORES["BLANCO"])
            self.pantalla.blit(sub, (boton.rect.x + 26, boton.rect.y + 103))

    def _dibujar_card_con_imagen(
        self,
        rect: pygame.Rect,
        color: Tuple[int, int, int],
        titulo: str,
        descripcion: str,
        imagen: Optional[pygame.Surface],
        estado: str,
        activa: bool,
    ):
        mouse = pygame.mouse.get_pos()
        hover = rect.collidepoint(mouse)

        color_base = color if not activa else COLORES["VERDE_OSCURO"]
        color_final = aclarar(color_base, 16) if hover else color_base

        sombra = rect.move(0, 4)
        pygame.draw.rect(self.pantalla, (0, 0, 0, 70), sombra, border_radius=14)
        pygame.draw.rect(self.pantalla, color_final, rect, border_radius=14)
        pygame.draw.rect(self.pantalla, COLORES["BLANCO"], rect, 2, border_radius=14)

        if hover:
            halo = pygame.Surface((rect.width + 24, rect.height + 24), pygame.SRCALPHA)
            pygame.draw.rect(
                halo,
                (255, 255, 255, 26),
                (0, 0, rect.width + 24, rect.height + 24),
                border_radius=18,
            )
            self.pantalla.blit(halo, (rect.x - 12, rect.y - 12))

        img_rect = pygame.Rect(rect.x + 8, rect.y + 8, 280, rect.height - 16)
        if imagen is not None:
            self.pantalla.blit(imagen, img_rect)
        else:
            pygame.draw.rect(self.pantalla, COLORES["GRIS"], img_rect, border_radius=10)

        txt_x = img_rect.right + 20
        t = self.fuentes["botones"].render(titulo, True, COLORES["BLANCO"])
        d = self.fuentes["normal"].render(descripcion, True, COLORES["BLANCO"])
        self.pantalla.blit(t, (txt_x, rect.y + 24))
        self.pantalla.blit(d, (txt_x, rect.y + 70))

        badge = pygame.Rect(rect.right - 236, rect.y + rect.height - 46, 210, 30)
        pygame.draw.rect(self.pantalla, COLORES["CARBON"], badge, border_radius=8)
        pygame.draw.rect(self.pantalla, COLORES["BLANCO"], badge, 1, border_radius=8)
        btxt = self.fuentes["pequena"].render(estado, True, COLORES["BLANCO"])
        self.pantalla.blit(btxt, btxt.get_rect(center=badge.center))

    def _dibujar_investigar(self):
        self._dibujar_fondo((60, 74, 112))
        self._dibujar_header(
            "INVESTIGAR LOCACIONES",
            "Haz click sobre cualquier tarjeta grande para investigar.",
            COLORES["AZUL_BRILLANTE"],
            mostrar_volver=True,
        )

        for key, rect in self._rects_locaciones().items():
            data = LOCACIONES[key]
            visitada = key in self.locaciones_investigadas
            estado = "✓ INVESTIGADA" if visitada else "CLICK PARA INVESTIGAR"
            self._dibujar_card_con_imagen(
                rect,
                data["color"],
                data["nombre"],
                data["desc"],
                self.imagenes_locaciones.get(key),
                estado,
                visitada,
            )

    def _dibujar_interrogar(self):
        self._dibujar_fondo((88, 62, 54))
        self._dibujar_header(
            "INTERROGAR PERSONAJES",
            "Selecciona al sospechoso para escuchar su version.",
            COLORES["NARANJA_BRILLANTE"],
            mostrar_volver=True,
        )

        for key, rect in self._rects_personajes().items():
            data = PERSONAJES[key]
            interrogado = key in self.personajes_interrogados
            estado = "✓ INTERROGADO" if interrogado else "CLICK PARA INTERROGAR"
            self._dibujar_card_con_imagen(
                rect,
                data["color"],
                data["nombre"],
                data["descripcion"],
                self.imagenes_personajes.get(key),
                estado,
                interrogado,
            )

    def _dibujar_pistas(self):
        self._dibujar_fondo((94, 62, 112))
        self._dibujar_header(
            "PISTAS RECOPILADAS",
            "Evidencia real y descartes de la investigacion.",
            COLORES["MAGENTA"],
            mostrar_volver=True,
        )

        if not self.pistas_descubiertas:
            vacio = pygame.Rect(120, 240, 1260, 220)
            pygame.draw.rect(self.pantalla, COLORES["CARBON"], vacio, border_radius=16)
            pygame.draw.rect(self.pantalla, COLORES["BLANCO"], vacio, 2, border_radius=16)
            t = self.fuentes["subtitulo"].render("Aun no hay pistas", True, COLORES["BLANCO"])
            s = self.fuentes["normal"].render("Investiga e interroga para descubrir evidencia.", True, COLORES["CIAN"])
            self.pantalla.blit(t, t.get_rect(center=(self.ancho // 2, 320)))
            self.pantalla.blit(s, s.get_rect(center=(self.ancho // 2, 372)))
            return

        y = 132
        visibles = self.pistas_descubiertas[-6:]
        iconos = {"personaje": "🎭", "locacion": "📍", "arma": "⚔"}

        for pista in visibles:
            rect = pygame.Rect(52, y, 1396, 110)
            borde = COLORES["VERDE"] if pista["correcta"] else COLORES["NARANJA_BRILLANTE"]
            pygame.draw.rect(self.pantalla, COLORES["CARBON"], rect, border_radius=12)
            pygame.draw.rect(self.pantalla, borde, rect, 2, border_radius=12)

            icono = self.fuentes["subtitulo"].render(iconos.get(pista["tipo"], "•"), True, COLORES["AMARILLO"])
            self.pantalla.blit(icono, (72, y + 26))

            txt = self.fuentes["normal"].render(pista["texto"], True, COLORES["BLANCO"])
            self.pantalla.blit(txt, (138, y + 40))
            y += 126

    def _dibujar_veredicto(self):
        self._dibujar_fondo((58, 86, 82))
        self._dibujar_header(
            "EMITIR VEREDICTO",
            "Usa las flechas grandes para elegir personaje, locacion y arma.",
            COLORES["VERDE"],
            mostrar_volver=True,
        )

        rects = self._rects_veredicto()
        mouse = pygame.mouse.get_pos()

        etiquetas = {
            "personaje": "PERSONAJE SOSPECHOSO",
            "locacion": "LOCACION DEL CRIMEN",
            "arma": "ARMA UTILIZADA",
        }

        for tipo in ["personaje", "locacion", "arma"]:
            prev_rect = rects[f"{tipo}_prev"]
            next_rect = rects[f"{tipo}_next"]
            val_rect = rects[f"{tipo}_valor"]

            pygame.draw.rect(self.pantalla, COLORES["CARBON"], val_rect, border_radius=14)
            pygame.draw.rect(self.pantalla, COLORES["BLANCO"], val_rect, 2, border_radius=14)

            for flecha_rect, simbolo in [(prev_rect, "<"), (next_rect, ">")]:
                hover = flecha_rect.collidepoint(mouse)
                color = COLORES["AZUL_BRILLANTE"] if hover else COLORES["AZUL_PILTOVER"]
                pygame.draw.rect(self.pantalla, color, flecha_rect, border_radius=12)
                pygame.draw.rect(self.pantalla, COLORES["BLANCO"], flecha_rect, 2, border_radius=12)
                txt = self.fuentes["subtitulo"].render(simbolo, True, COLORES["BLANCO"])
                self.pantalla.blit(txt, txt.get_rect(center=flecha_rect.center))

            clave = self._actual_seleccion(tipo)
            if tipo == "personaje":
                titulo = PERSONAJES[clave]["nombre"]
                desc = PERSONAJES[clave]["descripcion"]
                img = self.imagenes_personajes.get(clave)
            elif tipo == "locacion":
                titulo = LOCACIONES[clave]["nombre"]
                desc = LOCACIONES[clave]["desc"]
                img = self.imagenes_locaciones.get(clave)
            else:
                titulo = ARMAS[clave]
                desc = "Seleccion de evidencia forense"
                img = None

            label = self.fuentes["pequena"].render(etiquetas[tipo], True, COLORES["CIAN"])
            self.pantalla.blit(label, (val_rect.x + 18, val_rect.y + 10))

            t = self.fuentes["botones"].render(titulo, True, COLORES["BLANCO"])
            d = self.fuentes["normal"].render(desc, True, COLORES["BLANCO"])
            self.pantalla.blit(t, (val_rect.x + 18, val_rect.y + 50))
            self.pantalla.blit(d, (val_rect.x + 18, val_rect.y + 96))

            if img is not None:
                self.pantalla.blit(img, (val_rect.right - 226, val_rect.y + 8))

        confirmar = rects["confirmar"]
        hover_c = confirmar.collidepoint(mouse)
        color_c = COLORES["VERDE"] if hover_c else COLORES["VERDE_OSCURO"]
        pygame.draw.rect(self.pantalla, color_c, confirmar, border_radius=14)
        pygame.draw.rect(self.pantalla, COLORES["BLANCO"], confirmar, 2, border_radius=14)
        texto = self.fuentes["botones"].render("CONFIRMAR VEREDICTO", True, COLORES["BLANCO"])
        self.pantalla.blit(texto, texto.get_rect(center=confirmar.center))

    def _dibujar_final(self):
        base = (44, 92, 64) if self.resultado_correcto else (116, 56, 56)
        self._dibujar_fondo(base)
        titulo = "CASO RESUELTO" if self.resultado_correcto else "VEREDICTO INCORRECTO"
        color = COLORES["VERDE"] if self.resultado_correcto else COLORES["ROJO"]
        self._dibujar_header(titulo, "Resultado de la investigacion", color)

        panel = pygame.Rect(180, 180, 1140, 470)
        pygame.draw.rect(self.pantalla, COLORES["CARBON"], panel, border_radius=16)
        pygame.draw.rect(self.pantalla, color, panel, 3, border_radius=16)

        msg = self.fuentes["subtitulo"].render(self.resultado_texto, True, COLORES["BLANCO"])
        self.pantalla.blit(msg, msg.get_rect(center=(self.ancho // 2, 250)))

        detalle = [
            f"Culpable real: {PERSONAJES[self.culpable]['nombre']}",
            f"Locacion real: {LOCACIONES[self.locacion_crimen]['nombre']}",
            f"Arma real: {ARMAS[self.arma_crimen]}",
        ]
        y = 340
        for linea in detalle:
            t = self.fuentes["normal"].render(linea, True, COLORES["BLANCO"])
            self.pantalla.blit(t, t.get_rect(center=(self.ancho // 2, y)))
            y += 74

        mouse = pygame.mouse.get_pos()
        self.botones_final["nuevo"].dibujar(self.pantalla, self.fuentes["botones"], mouse)
        self.botones_final["salir"].dibujar(self.pantalla, self.fuentes["botones"], mouse)

    # ------------------------------------------------------------------
    # EVENTOS
    # ------------------------------------------------------------------

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.corriendo = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    if self.pantalla_actual in {
                        Pantalla.INVESTIGAR,
                        Pantalla.INTERROGAR,
                        Pantalla.PISTAS,
                        Pantalla.VEREDICTO,
                    }:
                        self.pantalla_actual = Pantalla.MENU
                    elif self.pantalla_actual == Pantalla.MENU:
                        self.pantalla_actual = Pantalla.INICIO
                elif evento.key == pygame.K_RETURN and self.pantalla_actual == Pantalla.VEREDICTO:
                    self._emitir_veredicto()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = evento.pos

                if self.pantalla_actual == Pantalla.INICIO:
                    if self.botones_inicio["iniciar"].contiene(pos):
                        self._iniciar_juego()
                    elif self.botones_inicio["salir"].contiene(pos):
                        self.corriendo = False

                elif self.pantalla_actual == Pantalla.MENU:
                    if self.botones_menu["investigar"].contiene(pos):
                        self.pantalla_actual = Pantalla.INVESTIGAR
                    elif self.botones_menu["interrogar"].contiene(pos):
                        self.pantalla_actual = Pantalla.INTERROGAR
                    elif self.botones_menu["pistas"].contiene(pos):
                        self.pantalla_actual = Pantalla.PISTAS
                    elif self.botones_menu["veredicto"].contiene(pos):
                        self.pantalla_actual = Pantalla.VEREDICTO

                elif self.pantalla_actual == Pantalla.INVESTIGAR:
                    if self.boton_volver.contiene(pos):
                        self.pantalla_actual = Pantalla.MENU
                        continue
                    for key, rect in self._rects_locaciones().items():
                        if rect.collidepoint(pos):
                            self._investigar_locacion(key)
                            break

                elif self.pantalla_actual == Pantalla.INTERROGAR:
                    if self.boton_volver.contiene(pos):
                        self.pantalla_actual = Pantalla.MENU
                        continue
                    for key, rect in self._rects_personajes().items():
                        if rect.collidepoint(pos):
                            self._interrogar_personaje(key)
                            break

                elif self.pantalla_actual == Pantalla.PISTAS:
                    if self.boton_volver.contiene(pos):
                        self.pantalla_actual = Pantalla.MENU

                elif self.pantalla_actual == Pantalla.VEREDICTO:
                    if self.boton_volver.contiene(pos):
                        self.pantalla_actual = Pantalla.MENU
                        continue

                    rects = self._rects_veredicto()
                    for tipo in ["personaje", "locacion", "arma"]:
                        if rects[f"{tipo}_prev"].collidepoint(pos):
                            self._mover_selector(tipo, -1)
                            break
                        if rects[f"{tipo}_next"].collidepoint(pos):
                            self._mover_selector(tipo, 1)
                            break

                    if rects["confirmar"].collidepoint(pos):
                        self._emitir_veredicto()

                elif self.pantalla_actual == Pantalla.FINAL:
                    if self.botones_final["nuevo"].contiene(pos):
                        self._iniciar_juego()
                    elif self.botones_final["salir"].contiene(pos):
                        self.corriendo = False

    # ------------------------------------------------------------------
    # LOOP
    # ------------------------------------------------------------------

    def dibujar(self):
        if self.pantalla_actual == Pantalla.INICIO:
            self._dibujar_inicio()
        elif self.pantalla_actual == Pantalla.MENU:
            self._dibujar_menu()
        elif self.pantalla_actual == Pantalla.INVESTIGAR:
            self._dibujar_investigar()
        elif self.pantalla_actual == Pantalla.INTERROGAR:
            self._dibujar_interrogar()
        elif self.pantalla_actual == Pantalla.PISTAS:
            self._dibujar_pistas()
        elif self.pantalla_actual == Pantalla.VEREDICTO:
            self._dibujar_veredicto()
        elif self.pantalla_actual == Pantalla.FINAL:
            self._dibujar_final()

        self._dibujar_toast()
        pygame.display.flip()

    def ejecutar(self):
        while self.corriendo:
            self.manejar_eventos()
            self.dibujar()
            self.reloj.tick(60)

        pygame.quit()


if __name__ == "__main__":
    juego = ClueArcaneVisual()
    juego.ejecutar()
