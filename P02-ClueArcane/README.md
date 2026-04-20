# 🎭 CLUE ARCANE: El Misterio de Piltover y Zaun

Simulador interactivo del juego de mesa **"Clue"** ambientado en el universo de la serie **Arcane**.

## 📋 Descripción General

El jugador debe investigar un crimen en el universo de Arcane para descubrir:
- **¿Quién?** El culpable (uno de 5 personajes)
- **¿Dónde?** La locación del crimen (uno de 5 lugares)
- **¿Con qué?** El arma utilizada (uno de 5 armas)

Cada partida genera aleatoriamente una combinación única, y el jugador debe usar investigación e interrogatorios para resolver el caso.

---

## 🎮 Cómo Jugar

### Versión Terminal (Línea de comandos)
```bash
python ClueArcane.py
```

### Versión GUI (Interfaz Gráfica con Pygame)
```bash
pip install pygame  # Solo la primera vez
python ClueArcane_GUI.py
```

**Ventajas de la versión GUI:**
- ✨ Interfaz gráfica visual
- 🎨 Botones interactivos coloridos
- 🎵 Soporte para música y sonidos (opcional)
- 🖱️ Controles con mouse
- 🎭 Temática Arcane con colores específicos

**Nota**: Ambas versiones tienen exactamente la misma lógica de juego.
La GUI es solo una interfaz mejorada visualmente.

### Opciones del Menú Principal

1. **Investigar una locación** - Busca evidencia en lugares específicos
2. **Interrogar a un personaje** - Cuestiona a sospechosos para obtener pistas
3. **Ver pistas descubiertas** - Revisa todas las evidencias encontradas
4. **Emitir veredicto** - Haz tu acusación final (culpable, locación, arma)
5. **Salir del juego** - Abandona la partida

### Mecánica de Juego

- **Investigar**: Si encuentras la locación correcta, obtienes una pista positiva. Si no, la descartas.
- **Interrogar**: Si interrogas al culpable, obtiene una pista incriminatoria. Si no, lo descartas.
- **Veredicto**: Debes acusar correctamente a los 3 elementos (personaje, locación, arma) para ganar.

---

## 🎭 Elementos del Juego (Temática Arcane)

### 5 Personajes Sospechosos

| Personaje | Rol | Descripción |
|-----------|-----|-------------|
| **Vi** | Vigilante | Protectora de la resistencia de Zaun |
| **Jinx** | Inventora de Caos | Genio explosivo y caótico |
| **Jayce** | Consejero Hextech | Político ambicioso de Piltover |
| **Silco** | Industrial de Zaun | Padrino del comercio en la Subraun |
| **Mel Medarda** | Diplomática | Agente estratégica de Noxus |

### 5 Locaciones del Crimen

| Locación | Descripción |
|----------|-------------|
| **Laboratorio Hextech** | Centro de investigación mágica |
| **The Last Drop** | Bar de reuniones clandestinas |
| **Consejo de Piltover** | Sede del poder político |
| **Puente del Progreso** | Frontera entre ciudades |
| **Prisión de Stillwater** | Fortaleza de máxima seguridad |

### 5 Armas del Crimen

| Arma | Descripción |
|------|-------------|
| **Guanteletes Atlas** | Arma de combate hextech |
| **Lanzacohetes Espinas** | Explosivo caótico |
| **Jeringa de Shimmer** | Veneno que altera la realidad |
| **Núcleo Hextech** | Cristal de energía arcana |
| **Bomba de Fuego** | Explosivo incendiario |

---

## 🎬 Finales Narrativos (5 Historias Distintas)

Cada final varía según quién sea el culpable. Las historias son únicas y fieles al estilo de Arcane:

### ✨ FINAL 1: VI - La Justicia
*"Proteger a Zaun"*

Vi actuó por necesidad, protegiendo a su gente de una amenaza. El tribunal reconoce su motivación pero la condena a trabajar bajo vigilancia en Zaun.

### 💥 FINAL 2: JINX - El Caos
*"Boom"*

Jinx cometió el crimen como un "experimento". Su falta de arrepentimiento y risa psicótica la revelan como un peligro puro. Condenada pero sin remordimiento.

### ⚡ FINAL 3: JAYCE - La Ambición
*"El Progreso a Cualquier Costo"*

El Consejero Hextech elimina un obstáculo político. Descubierto, Piltover cae en caos. Jayce fue símbolo de brillo, ahora manchado de sangre.

### 🌑 FINAL 4: SILCO - El Padrino
*"Negocios de la Calle"*

Un ajuste de cuentas de Silco. Aunque culpable, el tribunal reconoce que es síntoma de un sistema corrupto. Su imperio continúa sin él.

### 🗡️ FINAL 5: MEL MEDARDA - La Estrategia
*"Noxus Siempre Gana"*

Mel fue agente de Noxus todo el tiempo, infiltrada en Piltover. Su crimen era estrategia política. Desaparece en las sombras antes de ser extraditada.

---

## 🏗️ Estructura del Código

```
ClueArcane.py
│
├── Clase ClueArcane
│   ├── Atributos de juego
│   │   ├── PERSONAJES (diccionario)
│   │   ├── LOCACIONES (diccionario)
│   │   ├── ARMAS (diccionario)
│   │   └── Variables de estado (pistas, descartados, etc.)
│   │
│   ├── Métodos de Control
│   │   ├── __init__() → Inicializa juego
│   │   ├── ejecutar_juego() → Bucle principal
│   │   └── mostrar_menu_principal() → Interfaz de usuario
│   │
│   ├── Métodos de Investigación
│   │   ├── investigar_locacion()
│   │   ├── _processar_investigacion_locacion()
│   │   ├── interrogar_personaje()
│   │   └── _processar_interrogatorio()
│   │
│   ├── Métodos de Pistas
│   │   └── ver_pistas()
│   │
│   ├── Métodos de Veredicto
│   │   ├── emitir_veredicto() → Captura acusación
│   │   ├── _mostrar_final_ganador() → Selector de historias
│   │   ├── _final_vi() → Historia 1
│   │   ├── _final_jinx() → Historia 2
│   │   ├── _final_jayce() → Historia 3
│   │   ├── _final_silco() → Historia 4
│   │   ├── _final_mel() → Historia 5
│   │   └── _mostrar_final_perdedor() → Derrota
│   │
│   └── función main() → Punto de entrada
```

---

## 📊 Diagrama de Flujo Conceptual

```
START
  │
  ├─→ Inicializar juego (random culpable, locación, arma)
  │
  ├─→ BUCLE PRINCIPAL
  │    │
  │    ├─→ Mostrar menú
  │    │
  │    ├─→ [1] Investigar locación
  │    │    └─→ Si es correcta → Pista positiva
  │    │    └─→ Si no → Descartar
  │    │
  │    ├─→ [2] Interrogar personaje
  │    │    └─→ Si es culpable → Pista incriminatoria
  │    │    └─→ Si no → Descartar
  │    │
  │    ├─→ [3] Ver pistas
  │    │    └─→ Mostrar descubrimientos
  │    │
  │    ├─→ [4] Emitir veredicto
  │    │    ├─→ Seleccionar culpable, locación, arma
  │    │    │
  │    │    ├─→ ¿Es correcto?
  │    │    │    ├─→ SÍ → Mostrar final ganador
  │    │    │    │        └─→ Seleccionar historia según culpable
  │    │    │    │        └─→ EXIT JUEGO
  │    │    │    │
  │    │    │    └─→ NO → Mostrar final perdedor
  │    │    │        └─→ Revelar solución
  │    │    │        └─→ EXIT JUEGO
  │    │
  │    └─→ [5] Salir del juego
  │         └─→ EXIT BUCLE
  │
  └─→ END
```

---

## 🔍 Lógica de Investigación

### Investigar Locación
```
├─ ¿Ya investigaste esta locación?
│  ├─ SÍ → Mensaje de "ya investigada"
│  └─ NO → Continuar
│
├─ ¿Es la locación correcta?
│  ├─ SÍ → Pista positiva + agregar a pistas descubiertas
│  └─ NO → Descartar locación
```

### Interrogar Personaje
```
├─ ¿Ya interrogaste este personaje?
│  ├─ SÍ → Mensaje de "ya interrogado"
│  └─ NO → Continuar
│
├─ ¿Es el culpable?
│  ├─ SÍ → Pista incriminatoria + agregar a pistas
│  └─ NO → Descartar personaje
```

---

## 💡 Ejemplo de Partida

```
1. Comienza la partida
   - Culpable aleatorio: Jinx
   - Locación aleatoria: The Last Drop
   - Arma aleatoria: Lanzacohetes Espinas

2. Jugador investiga "Laboratorio Hextech"
   - No encuentra nada → Se descarta

3. Jugador interroga a "Vi"
   - Vi tiene coartada → Se descarta

4. Jugador investiga "The Last Drop"
   - ¡Encuentra evidencia! → PISTA POSITIVA

5. Jugador interroga a "Jinx"
   - ¡Comportamiento sospechoso! → PISTA INCRIMINATORIA

6. Jugador emite veredicto:
   - Culpable: Jinx ✓
   - Locación: The Last Drop ✓
   - Arma: Lanzacohetes Espinas ✓
   
   ¡GANADOR! Se muestra el FINAL 2: JINX - El Caos Encarnado
```

---

## ⚙️ Requisitos Técnicos

### Versión Terminal (ClueArcane.py)
- **Python**: 3.8+
- **Módulos**: `random` (estándar), `typing` (estándar)
- **Plataforma**: Windows, macOS, Linux

### Versión GUI (ClueArcane_GUI.py)
- **Python**: 3.8+
- **Módulos**: `pygame` (instalar con `pip install pygame`)
- **Plataforma**: Windows, macOS, Linux

---

## � Agregar Sonidos e Imágenes (Opcional)

La versión GUI permite agregar recursos multimedia para mejorar la experiencia:

### 📁 Estructura de Assets
```
assets/
├── README.md           # Instrucciones detalladas
├── sonidos/           # Archivos de audio
│   └── musica_fondo.wav
│   └── pista_buena.wav
│   └── victoria.wav
│   └── derrota.wav
│   └── ... (otros SFX)
└── imagenes/          # Archivos de imagen
    └── fondo_piltover.png
    └── personaje_vi.png
    └── personaje_jinx.png
    └── ... (otros sprites)
```

### 📖 Instrucciones Completas

Ve a la carpeta `assets/` y lee el archivo `README.md` para:
- ✅ Qué archivos puedes agregar
- ✅ Formatos recomendados
- ✅ Dónde encontrar recursos gratuitos
- ✅ Cómo integrarlos en el juego

**Importante**: El juego funciona perfectamente **sin estos recursos**.
Son completamente opcionales y solo mejoran la experiencia.

---

✅ **Estructura orientada a objetos** - Clase `ClueArcane`  
✅ **Comentarios exhaustivos** - Cada sección está documentada  
✅ **Menú interactivo** - Interfaz user-friendly  
✅ **Validación de entrada** - Manejo de errores  
✅ **5 finales únicos** - Historias narrativas diferentes por culpable  
✅ **Sistema de pistas** - Descubrimientos acumulativos  
✅ **Temática Arcane** - Lore consistente con la serie  

### Características Adicionales (Versión GUI)
✅ **Interfaz gráfica con Pygame** - Pantallas visuales coloridas  
✅ **Botones interactivos** - Click y hover effects  
✅ **Colores temáticos Arcane** - Paleta personalizada  
✅ **Soporte de sonido** - Música y SFX (opcional, auto-detecta archivos)  
✅ **Múltiples pantallas** - Menú, investigación, pistas, final  
✅ **Manejo de eventos** - Mouse totalmente funcional  
✅ **Sistema de descubrimiento visual** - Pistas se muestran en tiempo real  

---

## 📁 Estructura de Archivos del Proyecto

```
P02-ClueArcane/
├── ClueArcane.py              # Versión terminal (original)
├── ClueArcane_GUI.py          # Versión gráfica (NUEVA con Pygame)
├── README.md                  # Esta documentación
├── DIAGRAMA_FLUJO.txt         # Diagramas detallados del programa
├── assets/                    # Carpeta de recursos multimedia
│   ├── README.md             # Instrucciones para agregar archivos
│   ├── sonidos/              # Archivos de audio (.wav, .mp3, .ogg)
│   └── imagenes/             # Archivos de imagen (.png, .jpg)
└── __pycache__/              # Archivos compilados de Python (auto-generado)
```

---

## 📝 Notas para Diagrama de Flujo

El código está estructurado con comentarios claros para facilitar la creación de un diagrama de flujo completo:

- **Fase 1**: Inicialización (líneas con "Constructor")
- **Fase 2**: Bucle principal (función `ejecutar_juego()`)
- **Fase 3**: Investigación (métodos `investigar_*` y `_processar_*`)
- **Fase 4**: Veredicto (método `emitir_veredicto()`)
- **Fase 5**: Finales narrativos (métodos `_final_*()`)

Cada función tiene un encabezado descriptivo que explica su propósito y flujo.

---

## 🎮 Controles

### Versión Terminal
- Ingresa números para seleccionar opciones del menú
- Presiona ENTER para confirmar
- Manejo de errores automático para entradas inválidas

### Versión GUI
- **Mouse**: Haz click en los botones para seleccionar opciones
- **Hover**: Los botones cambian de color cuando pasas el mouse
- **Click**: Haz click izquierdo para confirmar selección
- **ESC o Cierra la ventana**: Para salir del juego

---

**¡A investigar los misterios de Piltover y Zaun se dijo!** 🎭✨
