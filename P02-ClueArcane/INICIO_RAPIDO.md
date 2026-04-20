# ⚡ INICIO RÁPIDO - CLUE ARCANE

## 🚀 Opción 1: Versión Terminal (Más Simple)

### Paso 1: Abrir terminal en la carpeta del proyecto
```powershell
cd c:\Users\gomao\Documents\SE-SegunoParcial\P02-ClueArcane
```

### Paso 2: Ejecutar el juego
```powershell
python ClueArcane.py
```

### ✅ Listo
El juego comenzará en la terminal. Usa números para navegar el menú.

---

## 🎨 Opción 2: Versión GUI (Con Interfaz Gráfica)

### Paso 1: Instalar Pygame (solo la primera vez)
```powershell
pip install pygame
```

### Paso 2: Abrir terminal en la carpeta del proyecto
```powershell
cd c:\Users\gomao\Documents\SE-SegunoParcial\P02-ClueArcane
```

### Paso 3: Ejecutar el juego
```powershell
python ClueArcane_GUI.py
```

### ✅ Listo
Se abrirá una ventana con interfaz gráfica. Usa el mouse para hacer click en los botones.

---

## 🎵 Opcional: Agregar Música y Sonidos a la Versión GUI

1. Ve a la carpeta `assets/README.md`
2. Sigue las instrucciones para descargar archivos de sonido
3. Coloca los archivos en `assets/sonidos/`
4. El juego auto-detectará los archivos y los reproducirá

### Descarga automática (recomendada)

```powershell
cd c:\Users\gomao\Documents\SE-SegunoParcial\P02-ClueArcane
python descargar_assets_wikimedia.py
```

Esto descarga imágenes + música + efectos desde Wikimedia Commons a:

- `assets/externos/imagenes/`
- `assets/externos/sonidos/`

La GUI v4 prioriza esos assets automáticamente.

**Importante**: El juego funciona perfectamente **sin archivos de sonido**.

### Carga manual (si tú eliges cada imagen)

Si quieres controlar todo el arte manualmente, coloca tus archivos aquí:

- `assets/externos/imagenes/`
- `assets/externos/sonidos/`

La GUI v4 detecta estos nombres base (puede ser `.png/.jpg/.jpeg/.webp` para imágenes y `.ogg/.wav/.oga/.mp3` para audio):

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

Ejemplo:

- `assets/externos/imagenes/locacion_hextech.jpg`
- `assets/externos/imagenes/personaje_vi.png`
- `assets/externos/sonidos/musica_fondo.mp3`

---

## ❓ Comparación Rápida

| Característica | Terminal | GUI |
|---|---|---|
| **Interfaz** | Línea de comandos | Ventana gráfica |
| **Mouse** | ❌ No | ✅ Sí |
| **Sonido** | ❌ No | ⚠️ Opcional |
| **Instalación** | ✅ Fácil | ⚠️ Requiere Pygame |
| **Rendimiento** | 🚀 Muy rápido | ⚡ Rápido |
| **Experiencia** | 📝 Texto | 🎨 Visual |

**Recomendación**: Comienza con **Versión Terminal** si es tu primera vez.
Luego prueba la **Versión GUI** para una experiencia más visual.

---

## 🔧 Solucionar Problemas

### Error: "No module named 'pygame'"
```powershell
pip install pygame
```

### Error: "No module named 'ClueArcane'"
Asegúrate de estar en la carpeta correcta:
```powershell
cd c:\Users\gomao\Documents\SE-SegunoParcial\P02-ClueArcane
```

### La ventana GUI no aparece
- Espera 5 segundos (a veces tarda en iniciar)
- Intenta ejecutar nuevamente
- Verifica que Pygame esté instalado correctamente

### No hay sonido en la versión GUI
- Esto es normal si no has agregado archivos de sonido
- Todos los archivos en `assets/sonidos/` son opcionales
- El juego continúa sin sonido

---

## 🎭 ¡Diviértete!

Ambas versiones tienen exactamente la **misma lógica de juego**.
Elige la que prefieras y comienza a investigar el misterio de Piltover y Zaun.

**¿Podrás descubrir al culpable?** 🔍✨
