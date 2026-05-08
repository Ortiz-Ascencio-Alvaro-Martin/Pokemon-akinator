# 🎮 Pokémon Adivina Quién - Con Sistema de Aprendizaje

## 🌟 Nuevas Características

Este juego ahora incluye un **sistema de aprendizaje automático** que permite al juego:

1. **Base de Datos Expandida** 📚
   - Contiene todos los Pokémon de Generaciones 1-9
   - Solo muestra inicialmente los 151 Pokémon de Gen 1
   - Los demás están disponibles para aprendizaje

2. **Búsqueda Difusa (Fuzzy Matching)** 🔍
   - Cuando introduces un Pokémon desconocido, el juego usa **distancia de Levenshtein**
   - Sugiere los 5 Pokémon más similares
   - Tolera pequeños errores de escritura

3. **Aprendizaje Iterativo** 🧠
   - Cuando no encuentra coincidencia exacta, pide el nombre del Pokémon
   - Guarda la **ruta de preguntas** que llevó hasta ese Pokémon
   - En futuras sesiones, esas mismas preguntas guiarán correctamente al nuevo Pokémon
   - Los datos se guardan en **localStorage** (persistente)

4. **Integración Automática** ✨
   - Los nuevos Pokémon aprendidos se agregan automáticamente a la lista del juego
   - Las preguntas se reconstruyen dinámicamente

## 🎯 Cómo Funciona

### Flujo Normal (Con candidatos)
```
1. El juego hace preguntas estratégicas
2. Con cada respuesta, filtra Pokémon
3. Cuando queda 1, adivina el nombre
```

### Flujo de Aprendizaje (Sin candidatos)
```
1. No hay coincidencias → "¿Cuál era tu Pokémon?"
2. Escribes el nombre (ej: "pikachu")
3. Búsqueda difusa sugiere similares (ej: "pikachu 98%")
4. Haces clic en la sugerencia o confirmas
5. El juego:
   - Agrega el Pokémon a su lista
   - Guarda las preguntas que lo llevaron allí
   - Aprende la ruta para futuras partidas
```

## 🛠️ Archivos Principales

### `pokemon-db.js`
- **Base de datos** completa de Pokémon (Gen 1-9)
- **Algoritmo de búsqueda difusa** (Levenshtein distance)
- **Sistema PokemonLearningSystem** (guardar/cargar datos)

### `script-improved.js`
- Lógica del juego mejorada
- Integración del modal de aprendizaje
- Reconstrucción dinámica de preguntas

### `index.html`
- Modal para ingresar Pokémon desconocidos
- Lista de sugerencias difusas

### `style.css`
- Estilos del modal
- Animaciones de las sugerencias

## 🔧 Algoritmo de Búsqueda Difusa

```javascript
levenshteinDistance("pikachu", "pikachuu")  // Distancia: 1
fuzzyMatch("pikachu", pokemon)              // Score: 98%
```

- Compara caracteres entre nombres
- Calcula similaridad como porcentaje
- Solo acepta matches >= 60% de similitud

## 💾 Persistencia de Datos

Los datos aprendidos se guardan en **localStorage**:
```javascript
localStorage.setItem('pokemonLearning', JSON.stringify(learnedData))
```

Estructura:
```json
{
  "25": {
    "id": 25,
    "paths": [
      {"questions": [...], "timestamp": 1234567890},
      {"questions": [...], "timestamp": 1234567891}
    ],
    "frequency": 2
  }
}
```

## 🎓 Ejemplo de Aprendizaje

**Primera sesión - Falla:**
- Preguntas: ¿Legendario? NO → ¿Tipo Eléctrico? NO → ...
- Resultado: 0 candidatos
- Usuario: "Meowth"
- Sistema: Agrega Meowth, guarda la ruta

**Segunda sesión - Éxito:**
- Preguntas: ¿Legendario? NO → ¿Tipo Eléctrico? NO → ...
- Resultado: Meowth está en candidatos
- Sistema: Adivina correctamente

## 📊 Preguntas Disponibles

### Categoría 1: Atributos Básicos (Prioridad Alta)
- ¿Es legendario?
- ¿Puede evolucionar?

### Categoría 2: Tipos (18 tipos)
- ¿Es de tipo Agua/Fuego/Planta/...?
- ¿Tiene tipo Agua/Fuego/...?

### Categoría 3: Colores (12 colores)
- ¿Es de color Azul/Rojo/Verde/...?

### Categoría 4: Hábitats
- ¿Vive en Agua/Montaña/Bosque/...?

### Categoría 5-7: Atributos Específicos
- Rareza, Grupo de Huevo, Peso, Altura

## 🚀 Futuras Mejoras

- [ ] Entrenamiento de modelos con RL
- [ ] Análisis de preguntas más efectivas
- [ ] Sincronización en la nube
- [ ] Estadísticas de precisión
- [ ] Sistema de recompensas por enseñanzas

---

**¡Cuantos más Pokémon desconocidos le enseñes, mejor se vuelve el juego!** 🎮✨
