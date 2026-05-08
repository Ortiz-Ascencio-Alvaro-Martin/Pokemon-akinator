# 🏗️ Arquitectura del Sistema - Diagrama

## 📊 Flujo General del Juego

```
┌─────────────────────────────────────────────────────────────────┐
│                    INICIO DEL JUEGO                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  CARGAR DATOS                                                   │
│  ├── pokemonList (151 Pokémon Gen 1)                            │
│  ├── fullPokemonList (950+ Pokémon Gen 1-9)                     │
│  ├── learningSystem (datos de aprendizaje previo)               │
│  └── questions (80+ preguntas disponibles)                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  MOSTRAR CUADRÍCULA DE POKÉMON                                  │
│  └── Todos los candidatos activos (inicialmente: 151)           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                              ✓ Lista para jugar
```

---

## 🎮 Flujo de Juego (Ronda Típica)

```
                    ┌─────────────────────────┐
                    │  USUARIO PIENSA EN UN   │
                    │     POKÉMON             │
                    └─────────────────────────┘
                              ↓
          ┌───────────────────────────────────────────┐
          │    JUEGO: ¿Es legendario?                 │
          │    (Pregunta con máxima entropía)         │
          └───────────────────────────────────────────┘
                              ↓
                    ┌─────────────────────────┐
                    │  USUARIO: SÍ o NO       │
                    └─────────────────────────┘
                              ↓
          ┌───────────────────────────────────────────┐
          │  FILTRAR CANDIDATOS                       │
          │  └── candidates = candidates.filter(...) │
          └───────────────────────────────────────────┘
                              ↓
          ┌───────────────────────────────────────────┐
          │  ¿CUÁNTOS CANDIDATOS QUEDAN?              │
          └───────────────────────────────────────────┘
              ↙                    ↓                    ↘
         MUCHOS              ALGUNOS                  UNO
            ↓                  ↓                       ↓
        SEGUIR              SEGUIR              ¡ADIVINADO!
       PREGUN-             PREGUN-              ✓ Éxito
        TANDO              TANDO                ↓ Reiniciar

              ↙ 0 CANDIDATOS
              │
         ¡PROBLEMA!
              ↓
     ┌─────────────────────┐
     │  MODAL APRENDIZAJE  │
     │ "¿Cuál era tu       │
     │  Pokémon?"          │
     └─────────────────────┘
```

---

## 🧠 Flujo de Aprendizaje

```
┌──────────────────────────────────────────────────────────────┐
│                   0 CANDIDATOS                               │
└──────────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────┐
│  MOSTRAR MODAL                                               │
│  ├── Input de texto (ej: "pikachu")                          │
│  └── Botones: Confirmar / Cancelar                           │
└──────────────────────────────────────────────────────────────┘
                         ↓
        Usuario escribe nombre + presiona tecla
                         ↓
┌──────────────────────────────────────────────────────────────┐
│  BUSCAR CON FUZZY MATCHING                                   │
│                                                              │
│  Para cada Pokémon en fullPokemonList:                       │
│  ├── Calcular similitud (0-100%)                             │
│  ├── Aplicar Levenshtein Distance                            │
│  └── Filtrar >= 60% similitud                                │
│                                                              │
│  Resultado: Top 5 sugerencias                                │
└──────────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────┐
│  MOSTRAR SUGERENCIAS                                         │
│  ├── Pikachu (100% similar)                                  │
│  ├── Raichu (75% similar)                                    │
│  └── ...                                                     │
└──────────────────────────────────────────────────────────────┘
                         ↓
        Usuario hace clic en sugerencia
                         ↓
┌──────────────────────────────────────────────────────────────┐
│  SELECCIONAR POKÉMON                                         │
│                                                              │
│  1. AGREGAR A pokemonList                                    │
│  └── pokemonList.push(selectedPokemon)                       │
│                                                              │
│  2. APRENDER LA RUTA                                         │
│  └── learningSystem.learnPokemon(id, path)                   │
│      └── path = [                                            │
│            {question: "¿Legendario?", answer: false},        │
│            {question: "¿Tipo Normal?", answer: true},        │
│            ...                                               │
│          ]                                                   │
│                                                              │
│  3. GUARDAR EN STORAGE                                       │
│  └── localStorage.setItem('pokemonLearning', JSON.stringify) │
│                                                              │
│  4. RECONSTRUIR PREGUNTAS                                    │
│  └── questions = buildQuestions()                            │
│                                                              │
│  5. MOSTRAR CONFIRMACIÓN                                     │
│  └── "¡Perfecto! Aprendí que tu Pokémon era ..."            │
│                                                              │
│  6. CERRAR MODAL                                             │
│  └── hideLearningModal()                                     │
└──────────────────────────────────────────────────────────────┘
                         ↓
              REINICIAR JUEGO
```

---

## 🔍 Algoritmo de Búsqueda Difusa

```
INPUT: "pikachu"

┌──────────────────────────────────────────────────────────────┐
│  PARA CADA POKÉMON EN BD                                     │
│  {                                                           │
│    1. MATCH EXACTO                                           │
│       if (name === "pikachu") → score = 100                  │
│       else continue...                                       │
│                                                              │
│    2. CONTIENE COMO SUBSTRING                                │
│       if (name.includes("pikachu")) → score = 90             │
│       else continue...                                       │
│                                                              │
│    3. LEVENSHTEIN DISTANCE (ediciones mínimas)               │
│       distance = levenshteinDistance("pikachu", name)        │
│       similarity = 100 - (distance / maxLen * 100)           │
│       score = similarity                                     │
│  }                                                           │
│                                                              │
│  MANTENER SI score >= 60%                                    │
└──────────────────────────────────────────────────────────────┘

EJEMPLO CON RESULTADOS:
"pikachu" vs...
├── "pikachu"     → Distancia: 0 → Score: 100 ✅ ACEPTADO
├── "pikachi"     → Distancia: 1 → Score: 89  ✅ ACEPTADO
├── "raichu"      → Distancia: 4 → Score: 44  ❌ RECHAZADO
└── "charizard"   → Distancia: 8 → Score: 20  ❌ RECHAZADO
```

---

## 💾 Estructura de localStorage

```
localStorage.getItem('pokemonLearning')

{
  "25": {                              ← ID del Pokémon (Pikachu)
    "id": 25,
    "paths": [                         ← Rutas que lo llevan aquí
      {
        "questions": [
          {
            "question": "¿Es legendario?",
            "answer": false
          },
          {
            "question": "¿Tipo eléctrico?",
            "answer": true
          },
          {
            "question": "¿Vive en bosque?",
            "answer": true
          }
        ],
        "timestamp": 1704067200000    ← Cuándo aprendió
      },
      {
        "questions": [...],
        "timestamp": 1704153600000
      }
    ],
    "frequency": 2                     ← Cuántas veces lo enseñaste
  },
  "152": {
    "id": 152,
    "paths": [...],
    "frequency": 1
  }
}
```

---

## 🎯 Selección de Preguntas (Algoritmo Entropy)

```
TENEMOS: 20 candidatos
PREGUNTAS NO HECHAS: 15

┌──────────────────────────────────────────────────────────────┐
│  PARA CADA PREGUNTA:                                         │
│                                                              │
│  1. CONTAR RESPUESTAS                                        │
│     yesCount = cuántos candidatos responden SÍ               │
│     noCount = cuántos candidatos responden NO                │
│                                                              │
│     Ej: "¿Tipo agua?"                                        │
│     yesCount = 7 (Squirtle, Psyduck, ...)                    │
│     noCount = 13 (Pikachu, Charmeleon, ...)                  │
│                                                              │
│  2. CALCULAR ENTROPÍA                                        │
│     p = yesCount / (yesCount + noCount) = 7/20 = 0.35        │
│     entropy = -[p*log2(p) + (1-p)*log2(1-p)]                 │
│            = -[0.35*log2(0.35) + 0.65*log2(0.65)]            │
│            = 0.93 (máximo en 0.5, mínimo en 0 o 1)           │
│                                                              │
│  3. CALCULAR SCORE FINAL                                     │
│     score = (prioridad) + (entropy * 0.5) + (log(count))     │
└──────────────────────────────────────────────────────────────┘

EJEMPLO DE COMPARACIÓN:

"¿Tipo agua?"           "¿Color verde?"
├─ SÍ: 7                ├─ SÍ: 12
├─ NO: 13               ├─ NO: 8
├─ Entropy: 0.93        ├─ Entropy: 0.98
├─ Score: 4.2           └─ Score: 4.8 ← MEJOR

ELEGIR LA DE MAYOR SCORE → "¿Color verde?"
```

---

## 📁 Árbol de Archivos Completo

```
P01-pokemon-game/
│
├── 🎮 EJECUTABLES
│   ├── index.html                    [HTTP: GET / → main.html]
│   ├── style.css                     [CSS global]
│   ├── pokemon-db.js                 [Base de datos + utils]
│   ├── script-improved.js            [Lógica principal]
│   └── script.js                     [Original, sin cambios]
│
├── 📚 DOCUMENTACIÓN
│   ├── COMIENZA_AQUI.md              ← EMPIEZA AQUI
│   ├── INDICE_DOCUMENTACION.md       ← Mapa de docs
│   ├── RESUMEN_EJECUTIVO.md          ← Visión gral
│   ├── README_LEARNING.md            ← Guía usuario
│   ├── IMPLEMENTACION_APRENDIZAJE.md ← Detalles técnicos
│   ├── REFERENCIA_TECNICA.md         ← API reference
│   ├── GUIA_PRUEBAS.md               ← Testing
│   ├── ARQUITECTURA.md               ← Este archivo
│   └── README.md                     [Original]
│
└── 📦 OTROS
    ├── pokemon-game/                 [Ignorar]
    └── script_temp.js                [Ignorar]
```

---

## 🔄 Ciclo de Vida de una Sesión

```
INICIO
  ↓
┌─────────────────────────────────┐
│ 1. CARGAR ESTADO PREVIO         │
│    - pokemonList               │
│    - learningSystem (datos)    │
│    - questions                 │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ 2. RENDERIZAR UI                │
│    - Cuadrícula de Pokémon      │
│    - Botones SÍ/NO             │
│    - Mensaje inicial            │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ 3. BUCLE PRINCIPAL              │
│    REPETIR:                     │
│    ├─ Hacer pregunta            │
│    ├─ Esperar respuesta         │
│    ├─ Filtrar candidatos        │
│    └─ ¿0 candidatos?            │
│       ├─ NO → Continuar bucle   │
│       └─ SÍ → Ir a 4            │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ 4. FLUJO DE APRENDIZAJE         │
│    ├─ Mostrar modal             │
│    ├─ Usuario ingresa nombre    │
│    ├─ Fuzzy match               │
│    ├─ Seleccionar Pokémon       │
│    ├─ Guardar datos             │
│    └─ Ir a 2 (reiniciar)        │
└─────────────────────────────────┘
  ↓
REPETIR INDEFINIDAMENTE
```

---

## 🧩 Componentes Principales

```
┌─────────────────────────────────────────────────────────────┐
│                    APLICACIÓN                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 1. BASE DE DATOS (pokemon-db.js)                    │  │
│  │    ├─ fullPokemonList (950+ Pokémon)               │  │
│  │    ├─ fuzzyMatch()                                  │  │
│  │    ├─ levenshteinDistance()                        │  │
│  │    └─ PokemonLearningSystem                        │  │
│  └──────────────────────────────────────────────────────┘  │
│                         ↓                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 2. LÓGICA DEL JUEGO (script-improved.js)           │  │
│  │    ├─ Selección de preguntas (entropy)             │  │
│  │    ├─ Filtrado de candidatos                       │  │
│  │    ├─ Gestión de respuestas                        │  │
│  │    └─ Sistema de aprendizaje                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                         ↓                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 3. INTERFAZ (index.html + style.css)               │  │
│  │    ├─ Cuadrícula de Pokémon                        │  │
│  │    ├─ Botones SÍ/NO                                │  │
│  │    ├─ Modal de aprendizaje                         │  │
│  │    └─ Sugerencias difusas                          │  │
│  └──────────────────────────────────────────────────────┘  │
│                         ↓                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 4. ALMACENAMIENTO (localStorage)                   │  │
│  │    └─ Datos de aprendizaje persistentes            │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Matriz de Decisión

```
            LEGENDARIO?
                 ↙  ↘
              SÍ       NO
              ↓        ↓
             [3]      [148]
              
              [Pokémon]  → ¿TIPO AGUA?
                           ↙        ↘
                          SÍ          NO
                          ↓           ↓
                        [2]         [146]
                        ↓            ↓
                      [Pokémon]     [Pokémon]
                          ↓            ↓
                    ... más preguntas ...
```

---

## 📈 Flujo de Datos

```
USUARIO INPUT (SÍ/NO)
    ↓
HANDLER: handleAnswer()
    ↓
FILTRAR: candidates.filter()
    ↓
ACTUALIZAR: currentSessionPath.push()
    ↓
RENDERIZAR: renderGrid()
    ↓
DECIDIR: askOrGuess()
    ├─ 1 candidato → Adivina
    ├─ 0 candidatos → Modal de aprendizaje
    └─ Muchos → Siguiente pregunta
    ↓
SIGUIENTE CICLO O APRENDIZAJE
    ├─ Si aprende → learningSystem.learnPokemon()
    ├─ Guardar → localStorage.setItem()
    └─ Reconstruir → questions = buildQuestions()
```

---

**¡Arquitectura lista para producción!** 🏗️✨
