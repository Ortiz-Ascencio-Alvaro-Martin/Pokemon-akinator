# 📂 ASSETS - Recursos Multimedia para CLUE ARCANE

Esta carpeta contiene los recursos multimedia del juego: imágenes y sonidos.

## 🎵 Carpeta: sonidos/

Aquí debes agregar archivos de audio para el juego.

### Archivos Esperados

| Archivo | Tipo | Descripción | Formato |
|---------|------|-------------|---------|
| `musica_fondo.wav` | Música | Música de fondo del juego | .wav, .mp3, .ogg |
| `pista_buena.wav` | SFX | Sonido cuando encuentras una pista | .wav |
| `investigacion.wav` | SFX | Sonido al investigar una locación | .wav |
| `interrogatorio.wav` | SFX | Sonido al interrogar un personaje | .wav |
| `veredicto.wav` | SFX | Sonido cuando emites veredicto | .wav |
| `victoria.wav` | SFX | Sonido cuando ganas | .wav |
| `derrota.wav` | SFX | Sonido cuando pierdes | .wav |

### Recomendaciones

- **Música de Fondo**: usa música libre con licencia compatible para videojuegos
- **Efectos de Sonido**: prioriza efectos en .ogg o .wav
- **Formatos**: .ogg y .wav son los más estables con Pygame
- **Duración**:
  - Música: 1-3 minutos (loop continuo)
  - SFX: 0.2-1 segundo

### Fuentes Recomendadas (Licencias Libres)

- **Wikimedia Commons** - Imágenes, música y sonidos libres
- **OpenGameArt** - Assets para juegos con licencias abiertas
- **Pixabay** - Imágenes/audio con licencia simple

---

## 🖼️ Carpeta: imagenes/

Aquí debes agregar archivos de imagen para el juego.

### Archivos Esperados (Opcional)

| Archivo | Descripción | Formato |
|---------|-------------|---------|
| `fondo_piltover.png` | Fondo temático de Piltover | .png, .jpg |
| `fondo_zaun.png` | Fondo temático de Zaun | .png, .jpg |
| `personaje_vi.png` | Retrato de Vi | .png |
| `personaje_jinx.png` | Retrato de Jinx | .png |
| `personaje_jayce.png` | Retrato de Jayce | .png |
| `personaje_silco.png` | Retrato de Silco | .png |
| `personaje_mel.png` | Retrato de Mel Medarda | .png |
| `icono_investigacion.png` | Ícono de investigación | .png |
| `icono_interrogatorio.png` | Ícono de interrogatorio | .png |

### Recomendaciones

- **Resolución**: 
  - Fondos: 1200x800 (resolución de pantalla)
  - Personajes: 200x300 (retratos)
  - Íconos: 64x64 o 128x128
  
- **Formatos**: .png (con transparencia) o .jpg
- **Inspiración**: Busca arte fan de Arcane o crea imágenes temáticas
- **Estilo**: Mantén coherencia con la estética oscura y colorida de Arcane

### Dónde Encontrar Imágenes

- **Pinterest** - Busca "Arcane fan art"
- **DeviantArt** - Comunidad de artistas
- **Google Images** - Busca con respeto de derechos (filtro de Creative Commons)
- **Canva** - Crea imágenes propias con diseño gráfico
- **Pixabay/Unsplash** - Imágenes libres de derechos

---

## 🔧 Cómo Usar

El código de `ClueArcane_GUI.py` intenta cargar automáticamente:

```powershell
# Descarga automática de assets externos libres (Wikimedia Commons)
cd c:\Users\gomao\Documents\SE-SegunoParcial\P02-ClueArcane
python descargar_assets_wikimedia.py
```

La GUI v4 intenta cargar assets en este orden:

1. `assets/externos/imagenes` y `assets/externos/sonidos`
2. `assets/imagenes` y `assets/sonidos`
3. Fallback visual/sonoro generado por el proyecto

### Carga manual recomendada para GUI v4

Si prefieres elegir cada archivo tú mismo, usa `assets/externos/` y respeta estos nombres base:

**Imágenes de locaciones**

- `locacion_hextech`
- `locacion_last_drop`
- `locacion_consejo`
- `locacion_puente`
- `locacion_prision`

**Imágenes de personajes**

- `personaje_vi`
- `personaje_jinx`
- `personaje_jayce`
- `personaje_silco`
- `personaje_mel`

**Audio**

- `musica_fondo`
- `pista_buena`
- `error`
- `investigacion`
- `interrogatorio`
- `victoria`
- `derrota`

Extensiones detectadas automáticamente:

- Imágenes: `.png`, `.jpg`, `.jpeg`, `.webp`
- Audio: `.ogg`, `.wav`, `.oga`, `.mp3`

Ejemplos válidos:

- `assets/externos/imagenes/locacion_hextech.jpg`
- `assets/externos/imagenes/personaje_vi.png`
- `assets/externos/sonidos/musica_fondo.mp3`

Archivos de referencia que se generan al descargar assets externos:

- `assets/externos/manifest.json`
- `assets/externos/CREDITOS_ASSETS_EXTERNOS.md`

**Si el archivo NO existe**, el juego continúa sin sonido (es totalmente funcional).

Para agregar tus recursos:

1. **Descarga o crea** los archivos de sonido/imagen
2. **Coloca los archivos** en esta carpeta (`assets/sonidos/` o `assets/imagenes/`)
3. **Ajusta los nombres** si usas nombres diferentes
4. **Abre `ClueArcane_GUI.py`** y actualiza las rutas si es necesario

---

## 📝 Nota Importante

El juego **funciona perfectamente SIN archivos multimedia**. Los archivos en esta carpeta son **completamente opcionales** y solo mejoran la experiencia visual y de audio.

Si el juego no encuentra los archivos, simplemente:
- Continúa sin música de fondo
- Continúa sin efectos de sonido
- Muestra la interfaz gráfica normal

¡Eso es todo! Disfruta del juego. 🎭✨
