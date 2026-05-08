# 🔧 Referencia Técnica Rápida

## 📦 APIs Principales

### 1. Base de Datos
```javascript
// Acceso global a lista completa
fullPokemonList   // Array de 950+ Pokémon

// Lista actual del juego
pokemonList       // Array de ~151 Pokémon

// Estructura de Pokémon:
{
  id: 25,
  name: "pikachu",
  tipo1: "eléctrico",
  tipo2: null,
  color: "amarillo",
  evoluciona: true,
  legendario: false,
  habitat: "bosque",
  peso: 6.0,
  altura: 0.4,
  huevo: "campo",
  rareza: "común"
}
```

### 2. Búsqueda Difusa
```javascript
// Buscar por nombre con tolerancia
findPokemonByName("pikachu")
// → { pokemon: {...}, score: 100 }

findPokemonByName("pikachi")  // Typo
// → { pokemon: {...}, score: 85 }

findPokemonByName("zzzzz")  // Muy diferente
// → null

// Scoring individual
fuzzyMatch("pikachu", pokemonObj)
// → 100 (0-100)

// Distancia de Levenshtein
levenshteinDistance("pikachu", "pikachi")
// → 1
```

### 3. Sistema de Aprendizaje
```javascript
// Instancia global
learningSystem   // PokemonLearningSystem

// Guardar que Pokémon fue aprendido
learningSystem.learnPokemon(pokemonId, questionPath)
// questionPath: [{question: "¿Legendario?", answer: false}, ...]

// Obtener Pokémon no jugados
learningSystem.getUnplayedPokemons(playedList)

// Datos aprendidos
learningSystem.learnedData
// {
//   "25": {
//     id: 25,
//     paths: [{questions: [...], timestamp: ...}],
//     frequency: 2
//   }
// }

// Guardar en localStorage
learningSystem.saveLearningData()

// Cargar de localStorage
learningSystem.loadLearningData()
```

### 4. Juego
```javascript
// Estado actual
candidates         // Pokémon que cumplen condiciones
asked              // Preguntas ya hechas
currentQuestion    // Pregunta actual
currentSessionPath // Ruta de preguntas de esta sesión

// Preguntas disponibles
questions          // Array de 80+ preguntas

// Hacer pregunta al usuario
nextQuestion()  // → "¿Es legendario?"

// Procesar respuesta
handleAnswer(true)   // Respuesta SÍ
handleAnswer(false)  // Respuesta NO

// Obtener mejores candidatos
renderGrid()

// Decidir si preguntar o adivinar
askOrGuess()

// Reiniciar
restartGame()
```

### 5. Interfaz de Aprendizaje
```javascript
// Mostrar modal
showLearningModal()

// Ocultar modal
hideLearningModal()

// Mostrar sugerencias
showFuzzySuggestions("pikachu")

// Seleccionar Pokémon
selectPokemon(pokemonObj)
```

---

## 🎯 Flujos Principales

### Flujo 1: Inicialización
```javascript
window.onload = () => {
  candidates = [...pokemonList]
  asked = []
  currentQuestion = null
  currentSessionPath = []
  renderGrid()
  questions = buildQuestions()
}
```

### Flujo 2: Respuesta del Usuario
```javascript
handleAnswer(isYes) {
  // Si no hay pregunta, hacer la primera
  if (!currentQuestion) {
    currentQuestion = pickBestQuestion()
    return
  }
  
  // Grabar respuesta
  asked.push(currentQuestion.text)
  currentSessionPath.push({question, answer})
  
  // Filtrar candidatos
  candidates = candidates.filter(pk => ...)
  
  // Renderizar y decidir
  renderGrid()
  askOrGuess()
}
```

### Flujo 3: Aprendizaje
```javascript
showLearningModal()  // Modal aparece

// Usuario escribe: "pikachu"
showFuzzySuggestions("pikachu")  // Muestra sugerencias

// Usuario elige: Pikachu
selectPokemon(pikachuObj) {
  // 1. Agregar a lista
  pokemonList.push(pikachu)
  
  // 2. Aprender ruta
  learningSystem.learnPokemon(25, currentSessionPath)
  
  // 3. Guardar datos
  learningSystem.saveLearningData()
  
  // 4. Reconstruir preguntas
  questions = buildQuestions()
  
  // 5. Limpiar modal
  hideLearningModal()
}
```

---

## 🧮 Algoritmos

### Levenshtein Distance
```javascript
levenshteinDistance(a, b) {
  // Matriz DP
  // Retorna número de ediciones
  // Ediciones: insert, delete, replace
  
  // Ejemplo:
  // "pikachu" → "pikachi"
  // 1 edición (replace 'u' por 'i')
  // Distancia: 1
}
```

### Fuzzy Matching
```javascript
fuzzyMatch(query, pokemon) {
  // 1. Match exacto → 100%
  // 2. Contiene → 90%
  // 3. Levenshtein normalizado → 0-100%
  
  // Retorna % similaridad
  // Umbral de aceptación: >= 60%
}
```

### Entropy para Preguntas
```javascript
entropy(p) {
  // p = probabilidad de SÍ
  // Mide incertidumbre
  // Max en p=0.5 (pregunta balanceada)
  // Min en p=0 o p=1 (pregunta inútil)
  
  return -(p*log2(p) + (1-p)*log2(1-p))
}

pickBestQuestion() {
  // Para cada pregunta no hecha:
  // 1. Calcular % candidatos que dicen SÍ
  // 2. Calcular entropía
  // 3. Elegir la con mayor entropía
  // Tie-breaker: prioridad, entropía, cardinalidad
}
```

---

## 💾 localStorage

### Estructura
```javascript
// Clave: "pokemonLearning"
{
  "25": {  // ID del Pokémon
    id: 25,
    paths: [
      {
        questions: [
          {question: "¿Es legendario?", answer: false},
          {question: "¿Tipo eléctrico?", answer: true}
        ],
        timestamp: 1704067200000
      }
    ],
    frequency: 1
  }
}
```

### Guardar
```javascript
learningSystem.saveLearningData()
// Actualiza localStorage

localStorage.setItem('pokemonLearning', JSON.stringify(learnedData))
```

### Cargar
```javascript
const data = localStorage.getItem('pokemonLearning')
// Retorna JSON string o null

const parsed = JSON.parse(data || '{}')
// Convierte a objeto
```

---

## 🎨 Elementos DOM

### IDs Principales
```html
<!-- Preguntas -->
<div id="question-text">Piensa en un Pokémon...</div>
<div id="question">¿Es legendario?</div>

<!-- Botones -->
<button id="yes-btn">SÍ</button>
<button id="no-btn">NO</button>
<button id="restart-btn">Reiniciar</button>
<button id="sound-toggle">🔊</button>

<!-- Cuadrícula -->
<div id="pokemon-grid">
  <div class="pokemon-card">
    <img src="...">
    <div class="poke-name">Pikachu</div>
  </div>
</div>

<!-- Modal -->
<div id="learning-modal" class="modal hidden">
  <div class="modal-content">
    <h2>¿Cuál era tu Pokémon?</h2>
    <input id="pokemon-input" type="text">
    <button id="submit-pokemon">Confirmar</button>
    <button id="cancel-learning">Cancelar</button>
    <div id="fuzzy-suggestions" class="suggestions hidden">
      <div id="suggestion-list"></div>
    </div>
  </div>
</div>
```

---

## 🔊 Sonidos

```javascript
SFX.click()       // Beep al hacer click
SFX.confirm()     // Beep doble confirmación
SFX.hover()       // Beep al pasar mouse
SFX.select()      // Beep de selección
SFX.startup()     // Beep de inicio

// Toggle
SFX.enabled = !SFX.enabled  // True/False
```

---

## 📊 Preguntas (buildQuestions)

### Categorías (en orden de prioridad)
1. **Legendario** (1 pregunta)
2. **Evolución** (1 pregunta)
3. **Tipo primario** (~18 preguntas)
4. **Tipo secundario** (~18 preguntas)
5. **Color** (~12 preguntas)
6. **Hábitat** (variable)
7. **Rareza** (2-3 preguntas)
8. **Grupo de huevo** (variable)
9. **Peso** (5+ preguntas)
10. **Altura** (4+ preguntas)

### Total: 80+ preguntas

---

## 🎯 Valores por Defecto

```javascript
// Inicio
pokemonList.length = 151  // Gen 1
fullPokemonList.length = 950+

// Búsqueda difusa
MIN_SIMILARITY = 60  // %

// Almacenamiento
STORAGE_KEY = 'pokemonLearning'

// Sonidos
SFX.enabled = true
SFX.gain = 0.12
```

---

## 🔧 Funciones Auxiliares

```javascript
capitalize(s)           // Capitaliza primer carácter
pokemonToObject([...])  // Convierte array a objeto

// Filtrado de candidatos
candidates.filter(pk => pk.tipo1 === 'agua')

// Búsqueda
pokemonList.find(p => p.id === 25)
pokemonList.filter(p => p.evoluciona)

// Conjuntos únicos
new Set(pokemonList.map(p => p.tipo1))
```

---

## ⚠️ Errores Comunes

### Error 1: pokemonList es undefined
```javascript
// Causa: script-improved.js no cargó
// Solución: Verificar que se importa DESPUÉS de pokemon-db.js
<script src="pokemon-db.js"></script>
<script src="script-improved.js"></script>
```

### Error 2: localStorage.getItem devuelve null
```javascript
// Causa: Primera vez ejecutando
// Solución: Verificar que no está en modo incógnito
if (!localStorage.getItem('pokemonLearning')) {
  localStorage.setItem('pokemonLearning', '{}')
}
```

### Error 3: Modal no desaparece
```javascript
// Causa: Falta llamar hideLearningModal()
// Solución: Verificar que selectPokemon() llama a hidden
document.getElementById('learning-modal').classList.add('hidden')
```

---

## 📈 Performance

| Operación | Tiempo |
|-----------|--------|
| Cargar página | <500ms |
| Hacer pregunta | <50ms |
| Búsqueda fuzzy | <100ms |
| Guardar localStorage | <50ms |
| Cargar localStorage | <50ms |

---

## 🚀 Deployment

### Requisitos
- HTML5 compatible browser
- JavaScript habilitado
- localStorage disponible
- ~500KB memoria

### Sin dependencias externas
- No necesita servidor
- No necesita base de datos
- Funciona offline
- Totalmente cliente-side

---

**¡Referencia lista para desarrollo!** 🎮✨
