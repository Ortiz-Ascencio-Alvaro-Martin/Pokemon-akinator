# 🧪 Guía de Pruebas - Sistema de Aprendizaje

## 🎯 Objetivo
Verificar que el sistema de aprendizaje funciona correctamente.

---

## 🚀 Pasos para Probar

### Requisitos
- Navegador moderno (Chrome, Firefox, Edge, Safari)
- Archivo `index.html` accesible localmente o via HTTP
- Consola del navegador disponible (F12)

### Prueba 1: Carga Básica
**Objetivo:** Verificar que el juego carga sin errores

1. Abre `index.html` en el navegador
2. Presiona F12 para abrir consola
3. **Esperado:**
   - No hay errores en rojo
   - Se ve el título "Pokémon Adivina Quién (Con Aprendizaje)"
   - Se muestra la cuadrícula de Pokémon
   - Botones SÍ/NO activos

```javascript
// En consola, verifica:
console.log(pokemonList.length)      // Debe ser 151
console.log(fullPokemonList.length)  // Debe ser > 500
console.log(questions.length)        // Debe ser > 50
```

### Prueba 2: Juego Normal (Sin Aprendizaje)
**Objetivo:** Verificar que el juego funciona normalmente

1. Piensa en **Pikachu**
2. Haz clic en SÍ/NO según corresponda:
   - ¿Es legendario? → NO
   - ¿Es de tipo eléctrico? → SÍ
   - Sigue respondiendo hasta que adivine
3. **Esperado:**
   - El juego elimina candidatos correctamente
   - Eventualmente dice "¡Tu Pokémon es Pikachu!"
   - Suena un beep confirmativo

### Prueba 3: Sistema de Aprendizaje (El Nuclear)
**Objetivo:** Verificar que aprende Pokémon nuevos

#### Paso A: Limpiar localStorage (opcional)
```javascript
// En consola:
localStorage.removeItem('pokemonLearning')
location.reload()
```

#### Paso B: Triggear el Aprendizaje
1. Piensa en un Pokémon que NO está en Gen 1
   - **Opciones:** Chikorita, Cyndaquil, Totodile (Gen 2)
   - O cualquiera de mi lista en `pokemon-db.js`

2. Responde las preguntas de forma que llegues a 0 candidatos
   - Ej: Si piensas "Chikorita":
     - ¿Legendario? → NO
     - ¿Tipo Agua? → NO
     - ¿Tipo Fuego? → NO
     - ¿Tipo Eléctrico? → NO
     - (etc., hasta que no haya candidatos)

3. **Verás el modal:** "¿Cuál era tu Pokémon?"

#### Paso C: Ingresa el Pokémon
1. Escribe en la caja de texto: `chikorita`
2. **Esperado:**
   - Se muestran sugerencias en tiempo real
   - Aparece "Chikorita (100% similar)" u otra opción
   - Puedes hacer clic en la sugerencia

3. Haz clic en "Chikorita"
4. **Esperado:**
   - El modal desaparece
   - Dice: "¡Perfecto! Aprendí que tu Pokémon era Chikorita. 📚"
   - Suena confirmación (beep positivo)

#### Paso D: Verifica Aprendizaje
```javascript
// En consola, verifica localStorage:
const data = JSON.parse(localStorage.getItem('pokemonLearning'))
console.log(data)  // Debe tener estructura con rutas

// También verifica que se agregó a la lista:
console.log(pokemonList.find(p => p.name === 'chikorita'))  // Debe existir
```

### Prueba 4: Búsqueda Difusa con Errores
**Objetivo:** Verificar que tolera errores de tipeo

1. Triggea el aprendizaje (mismos pasos, diferente Pokémon)
2. En el modal, escribe un nombre con error:
   - `cinarquil` en lugar de `chikorita`
   - `bulbosaur` en lugar de `bulbasaur`
   - `pikachu` en lugar de `pikachu` (escribe mal)

3. **Esperado:**
   - Las sugerencias muestran Pokémon similares
   - Porcentajes de similitud (<100%)
   - Ej: "Chikorita (87% similar)"

4. Selecciona la sugerencia
5. **Esperado:**
   - Se agrega correctamente
   - Funciona el aprendizaje

### Prueba 5: Segunda Sesión (Aprendizaje Persistente)
**Objetivo:** Verificar que el juego recuerda lo aprendido

1. Recarga la página (`F5` o `Ctrl+R`)
2. Piensa en el Pokémon que enseñaste antes (ej: Chikorita)
3. Responde las MISMAS preguntas que respondiste la primera vez
4. **Esperado:**
   - Esta vez debe aparecer en candidatos
   - El juego lo adivina directamente

```javascript
// En consola, verifica que aprendió:
const data = JSON.parse(localStorage.getItem('pokemonLearning'))
console.log(data['152'])  // Chikorita es ID 152
// Debe mostrar las preguntas que guardó
```

### Prueba 6: Múltiples Pokémon
**Objetivo:** Verificar que aprende varios

1. Repite Prueba 3 con diferentes Pokémon:
   - Cyndaquil (Gen 2)
   - Totodile (Gen 2)
   - Treecko (Gen 3)
   - Snivy (Gen 5)

2. **Esperado:**
   - Cada uno se agrega a la lista
   - `pokemonList.length` aumenta
   - localStorage guarda múltiples rutas

```javascript
// En consola:
const data = JSON.parse(localStorage.getItem('pokemonLearning'))
console.log(Object.keys(data).length)  // Debe ser >= 4
```

### Prueba 7: Reinicio
**Objetivo:** Verificar botón Reiniciar

1. Empieza un juego
2. Haz algunas preguntas
3. Haz clic en "Reiniciar"
4. **Esperado:**
   - Vuelve al estado inicial
   - Pregunta: "Piensa en un Pokémon..."
   - Todos los candidatos activos
   - Sin datos de sesión anterior

### Prueba 8: Sonidos
**Objetivo:** Verificar que los efectos de sonido funcionan

1. Haz clic en botones (SÍ/NO, Reiniciar)
2. **Esperado:**
   - Se escuchan beeps 8-bit
   - Botón 🔊 en la esquina

3. Haz clic en 🔊
4. **Esperado:**
   - Los sonidos se silencian
   - El botón cambia a 🔈

---

## 🐛 Problemas Comunes

### Problema 1: Modal no aparece
**Causa:** JavaScript no se cargó correctamente
**Solución:**
```javascript
// En consola:
console.log(typeof showLearningModal)  // Debe ser "function"
```

### Problema 2: Búsqueda no funciona
**Causa:** Pokémon no en BD
**Solución:**
```javascript
// Verifica que exista:
console.log(fullPokemonList.find(p => p.name === 'chikorita'))
```

### Problema 3: localStorage vacío
**Causa:** Navegador en modo incógnito
**Solución:** Abre en modo normal

### Problema 4: Estilos del modal feos
**Causa:** CSS no cargó
**Solución:** Verifica que `style.css` esté en la misma carpeta

---

## 📊 Casos de Prueba (Test Matrix)

| Caso | Entrada | Esperado | Status |
|------|---------|----------|--------|
| Carga | Abrir página | Sin errores | ⬜ |
| Juego Normal | Pikachu + SÍ/NO | Adivina Pikachu | ⬜ |
| Aprendizaje | Chikorita + Modal | Se agrega | ⬜ |
| Fuzzy | "chikorit" | Sugerencias | ⬜ |
| Persistencia | Recarga + mismo Pokémon | Lo adivina | ⬜ |
| Múltiples | 3+ Pokémon nuevos | Todos agregados | ⬜ |
| Reinicio | Botón Reiniciar | Vuelve al inicio | ⬜ |
| Sonidos | Botones + 🔊 | Sonidos activos | ⬜ |

---

## 📈 Métricas de Éxito

- ✅ Sistema de aprendizaje completamente funcional
- ✅ Búsqueda difusa con match >= 60%
- ✅ localStorage persistente entre sesiones
- ✅ Modal intuitivo y responsivo
- ✅ Sin errores en consola
- ✅ Sonidos funcionales
- ✅ Experiencia de usuario fluida

---

## 🎮 Script de Prueba Manual

```javascript
// Copiar y pegar en consola para prueba rápida

// 1. Ver estado inicial
console.log('=== ESTADO INICIAL ===')
console.log('Pokémon en juego:', pokemonList.length)
console.log('Pokémon en BD:', fullPokemonList.length)
console.log('Preguntas:', questions.length)

// 2. Ver datos aprendidos
console.log('\n=== DATOS APRENDIDOS ===')
const learned = JSON.parse(localStorage.getItem('pokemonLearning')) || {}
console.log('Pokémon enseñados:', Object.keys(learned).length)
console.log(learned)

// 3. Probar búsqueda difusa
console.log('\n=== BÚSQUEDA DIFUSA ===')
const result = findPokemonByName('pikachu')
console.log('Búsqueda "pikachu":', result)

const result2 = findPokemonByName('pika')
console.log('Búsqueda "pika":', result2)

// 4. Verifica estado de juego
console.log('\n=== ESTADO DE JUEGO ===')
console.log('Candidatos:', candidates.length)
console.log('Preguntas hechas:', asked.length)
```

---

## ✅ Checklist Final

- [ ] Página carga sin errores
- [ ] Juego funciona normalmente
- [ ] Modal aparece cuando no hay candidatos
- [ ] Búsqueda difusa funciona
- [ ] Se agrega Pokémon nuevo
- [ ] localStorage guarda datos
- [ ] Datos persisten tras recarga
- [ ] Sonidos funcionan
- [ ] Responsivo en móvil
- [ ] Botones responden

---

**¡Cuando todos los checks están verdes, el sistema está listo!** ✨
