// ===================================================================
// SISTEMA DE JUEGO CON APRENDIZAJE
// ===================================================================

// Inicializar con Gen 1 (151)
let pokemonList = fullPokemonList.slice(0, 151).map(p => ({ ...p }));
const basePokemonIds = new Set(pokemonList.map(p => p.id));

// Persistir Pokémon agregados por el usuario (para que no se pierdan al cerrar/abrir)
const addedPokemonsStorageKey = 'pokemonAddedToGame_v1';

function loadAddedPokemonIds() {
	try {
		const raw = localStorage.getItem(addedPokemonsStorageKey);
		if (!raw) return [];
		const parsed = JSON.parse(raw);
		if (!Array.isArray(parsed)) return [];
		return parsed
			.map(Number)
			.filter(id => Number.isFinite(id) && id > 0);
	} catch (e) {
		console.error('Error loading added pokemon ids:', e);
		return [];
	}
}

function saveAddedPokemonIds(ids) {
	try {
		const unique = Array.from(new Set(
			(ids || [])
				.map(Number)
				.filter(id => Number.isFinite(id) && id > 0)
		));
		localStorage.setItem(addedPokemonsStorageKey, JSON.stringify(unique));
	} catch (e) {
		console.error('Error saving added pokemon ids:', e);
	}
}

function rememberAddedPokemon(pokemon) {
	const id = Number(pokemon?.id);
	if (!Number.isFinite(id) || id <= 0) return;
	if (basePokemonIds.has(id)) return;

	const current = loadAddedPokemonIds();
	if (current.includes(id)) return;
	current.push(id);
	saveAddedPokemonIds(current);
}

async function syncStoredAddedPokemonsToGame() {
	const storedIds = loadAddedPokemonIds();
	for (const id of storedIds) {
		if (basePokemonIds.has(id)) continue;
		const storedPokemon = await ensurePokemonDetails(id);
		if (storedPokemon) {
			addPokemonToGame(storedPokemon);
		}
	}
}
const learningSystem = new PokemonLearningSystem();

let questions = [];
let candidates = [];
let asked = [];
let currentQuestion = null;
let currentSessionPath = []; // Guardar la ruta de preguntas de esta sesión
let pendingPokemon = null;
let awaitingGuessConfirmation = false;
let pendingGuessPokemon = null;

function capitalize(s) { return String(s).charAt(0).toUpperCase() + String(s).slice(1); }

function buildQuestions() {
	const qs = [];
	
	// 1️⃣ PREGUNTAS DIVERTIDAS Y COMUNES (prioritario)
	qs.push({ key: 'legendario', value: true, text: '¿Es legendario?' });
	qs.push({ key: 'evoluciona', value: true, text: '¿Puede evolucionar?' });

	// 2️⃣ PREGUNTAS SOBRE TIPOS
	const tipos = new Set();
	pokemonList.forEach(p => { if(p.tipo1) tipos.add(p.tipo1); if(p.tipo2) tipos.add(p.tipo2); });
	
	const tiposOrdenados = ['agua', 'fuego', 'planta', 'normal', 'eléctrico', 'psíquico', 'hielo', 'roca', 
							'tierra', 'volador', 'bicho', 'veneno', 'lucha', 'dragón', 'fantasma', 'acero', 'hada'];
	
	tiposOrdenados.forEach(t => {
		if (tipos.has(t)) {
			qs.push({ key: 'tipo1', value: t, text: `¿Es de tipo ${capitalize(t)}?` });
		}
	});
	
	tiposOrdenados.forEach(t => {
		if (tipos.has(t)) {
			qs.push({ key: 'tipo2', value: t, text: `¿Tiene tipo ${capitalize(t)}?` });
		}
	});

	// 3️⃣ PREGUNTAS SOBRE COLORES
	const colors = new Set(pokemonList.map(p => p.color).filter(Boolean));
	const coloresOrdenados = ['azul', 'rojo', 'verde', 'amarillo', 'naranja', 'rosa', 'morado', 'marrón', 
							   'gris', 'blanco', 'crema', 'negro'];
	
	coloresOrdenados.forEach(c => {
		if (colors.has(c)) {
			qs.push({ key: 'color', value: c, text: `¿Es de color ${capitalize(c)}?` });
		}
	});

	// 4️⃣ PREGUNTAS SOBRE HÁBITATS
	const habitats = new Set(pokemonList.map(p => p.habitat).filter(Boolean));
	habitats.forEach(h => qs.push({ key: 'habitat', value: h, text: `¿Vive en ${capitalize(h)}?` }));

	// 5️⃣ PREGUNTAS SOBRE RAREZA
	const rares = new Set(pokemonList.map(p => p.rareza).filter(Boolean));
	rares.forEach(r => qs.push({ key: 'rareza', value: r, text: `¿Es ${r} (rareza)?` }));

	// 6️⃣ PREGUNTAS SOBRE GRUPOS DE HUEVO
	const eggs = new Set(pokemonList.map(p => p.huevo).filter(Boolean));
	eggs.forEach(e => qs.push({ key: 'huevo', value: e, text: `¿Pertenece al grupo huevo ${capitalize(e)}?` }));

	// 7️⃣ PREGUNTAS SOBRE PESO Y ALTURA
	const pesoThresholds = [1, 5, 10, 20, 50, 100];
	pesoThresholds.forEach(th => qs.push({ key: 'peso', value: v => (v || 0) > th, text: `¿Pesa más de ${th}kg?` }));
	
	const alturaThresholds = [0.5, 1.0, 1.5, 2.0];
	alturaThresholds.forEach(th => qs.push({ key: 'altura', value: v => (v || 0) > th, text: `¿Mide más de ${th}m?` }));

	return qs;
}

function addPokemonToGame(pokemon) {
	let added = false;

	if (!pokemonList.some(p => p.id === pokemon.id)) {
		pokemonList.push({ ...pokemon });
		rememberAddedPokemon(pokemon);
		added = true;
	}

	if (!fullPokemonList.some(p => p.id === pokemon.id)) {
		fullPokemonList.push({ ...pokemon });
		added = true;
	}

	return added;
}

async function syncLearnedPokemonsToGame() {
	for (const pokemonId of Object.keys(learningSystem.learnedData)) {
		const learnedPokemon = await ensurePokemonDetails(Number(pokemonId));
		if (learnedPokemon) {
			addPokemonToGame(learnedPokemon);
		}
	}
}

questions = buildQuestions();

// --- Heurística: elegir la pregunta que mejor divide ---
function pickBestQuestion() {
	function entropy(p) {
		if (p <= 0 || p >= 1) return 0;
		return - (p * Math.log2(p) + (1 - p) * Math.log2(1 - p));
	}

	let best = null;
	let bestScore = -Infinity;
	for (const q of questions) {
		if (asked.includes(q.text)) continue;
		let yesCount = 0, noCount = 0;
		for (const pk of candidates) {
			let yes = false;
			if (typeof q.value === 'function') {
				try { yes = q.value(pk[q.key]); } catch (e) { yes = false; }
			} else {
				if (pk[q.key] === undefined) yes = false;
				else yes = pk[q.key] === q.value;
			}
			if (yes) yesCount++; else noCount++;
		}
		const total = yesCount + noCount;
		if (total === 0) continue;
		if (yesCount === 0 || noCount === 0) continue;

		const p = yesCount / total;
		const qEntropy = entropy(p);
		const qIndex = questions.indexOf(q);
		const score = (1 / (qIndex + 1)) + qEntropy * 0.5 + Math.log2(total + 1) * 0.01;

		if (score > bestScore) {
			bestScore = score;
			best = q;
		}
	}
	return best;
}

// --- Simple SFX ---
const SFX = {
	ctx: null,
	gain: null,
	musicGain: null,
	enabled: true,
	musicEnabled: true,

	init() {
		if (!this.ctx) {
			this.ctx = new (window.AudioContext || window.webkitAudioContext)();
			this.gain = this.ctx.createGain();
			this.gain.gain.value = 0.12;
			this.gain.connect(this.ctx.destination);
		}
	},

	playTone(freq, duration = 60) {
		if (!this.enabled) return;
		try {
			this.init();
			const o = this.ctx.createOscillator();
			o.type = 'sine';
			o.frequency.value = freq;
			o.connect(this.gain);
			o.start();
			o.stop(this.ctx.currentTime + duration/1000);
		} catch (e) { /* ignore */ }
	},

	click() { this.playTone(900, 40); },
	confirm() { this.playTone(520, 160); setTimeout(() => this.playTone(720, 120), 150); },
	hover() { this.playTone(1200, 25); },
	select() { this.playTone(600, 80); setTimeout(() => this.playTone(800, 80), 80); },
	startup() { this.playTone(400, 100); setTimeout(() => this.playTone(600, 150), 120); setTimeout(() => this.playTone(800, 100), 280); }
};

function syncAudioState() {
	const music = document.getElementById('background-music');
	const soundToggle = document.getElementById('sound-toggle');

	if (soundToggle) {
		soundToggle.textContent = SFX.enabled ? '🔊' : '🔈';
	}

	SFX.musicEnabled = SFX.enabled;

	if (!music) {
		return;
	}

	music.volume = 0.25;
	music.muted = !SFX.enabled;

	if (SFX.enabled) {
		music.play().catch(() => {});
	} else {
		music.pause();
	}
}

// --- Renderiza la cuadrícula de Pokémon ---
function renderGrid() {
	const grid = document.getElementById('pokemon-grid');
	grid.innerHTML = '';
	pokemonList.forEach(pk => {
		const isCandidate = candidates.includes(pk);
		const card = document.createElement('div');
		card.className = 'pokemon-card' + (isCandidate ? '' : ' inactive');
		card.innerHTML = `
			<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pk.id}.png" alt="${pk.name}">
			<div class="poke-name">${pk.name.charAt(0).toUpperCase() + pk.name.slice(1)}</div>
		`;
		card.title = `Tipo: ${pk.tipo1}${pk.tipo2 ? '/' + pk.tipo2 : ''}\nColor: ${pk.color}`;
		
		if (isCandidate) {
			card.addEventListener('mouseenter', () => SFX.hover());
			card.addEventListener('click', () => SFX.select());
		}
		
		grid.appendChild(card);
	});
}

function nextQuestion() {
	const q = pickBestQuestion();
	if (!q) { currentQuestion = null; return null; }
	currentQuestion = q;
	return q.text;
}

function handleAnswer(isYes) {
	if (awaitingGuessConfirmation) {
		handleGuessConfirmation(isYes);
		return;
	}

	// Si no hay pregunta actual, generar la primera pregunta
	if (!currentQuestion) {
		const q = pickBestQuestion();
		if (!q) return;
		currentQuestion = q;
		const qDiv = document.getElementById('question-text');
		qDiv.textContent = q.text;
		SFX.startup();
		return;
	}
	
	asked.push(currentQuestion.text);
	currentSessionPath.push({ question: currentQuestion.text, answer: isYes });
	
	if (typeof currentQuestion.value === 'function') {
		candidates = candidates.filter(pk =>
			isYes ? currentQuestion.value(pk[currentQuestion.key])
						: !currentQuestion.value(pk[currentQuestion.key])
		);
	} else {
		candidates = candidates.filter(pk =>
			isYes ? pk[currentQuestion.key] === currentQuestion.value
						: pk[currentQuestion.key] !== currentQuestion.value
		);
	}
	renderGrid();
	SFX.click();
	askOrGuess();
}

function askOrGuess() {
	const qText = nextQuestion();
	const qDiv = document.getElementById('question-text');
	const yesBtn = document.getElementById('yes-btn');
	const noBtn = document.getElementById('no-btn');
	
	if (candidates.length === 1) {
		pendingGuessPokemon = candidates[0];
		awaitingGuessConfirmation = true;
		qDiv.textContent = `¿Era ${pendingGuessPokemon.name.charAt(0).toUpperCase() + pendingGuessPokemon.name.slice(1)}?`;
		yesBtn.disabled = false;
		noBtn.disabled = false;
		SFX.confirm();
	} else if (candidates.length === 0) {
		// No hay coincidencias - activar modo aprendizaje
		qDiv.textContent = "Hmm... no encontré coincidencias. ¿Cuál era tu Pokémon?";
		yesBtn.disabled = true;
		noBtn.disabled = true;
		showLearningModal();
	} else if (qText) {
		qDiv.textContent = qText;
		yesBtn.disabled = false;
		noBtn.disabled = false;
	} else {
		qDiv.textContent = "No puedo hacer más preguntas. ¿Quieres reiniciar?";
		yesBtn.disabled = true;
		noBtn.disabled = true;
	}
}

function handleGuessConfirmation(isYes) {
	const qDiv = document.getElementById('question-text');
	const yesBtn = document.getElementById('yes-btn');
	const noBtn = document.getElementById('no-btn');

	awaitingGuessConfirmation = false;

	if (isYes && pendingGuessPokemon) {
		qDiv.textContent = `¡Tu Pokémon era ${pendingGuessPokemon.name.charAt(0).toUpperCase() + pendingGuessPokemon.name.slice(1)}!`;
		yesBtn.disabled = true;
		noBtn.disabled = true;
		SFX.confirm();
		pendingGuessPokemon = null;
		return;
	}

	pendingGuessPokemon = null;
	qDiv.textContent = "Entonces ayúdame a aprender cuál era.";
	yesBtn.disabled = true;
	noBtn.disabled = true;
	showLearningModal();
}

// --- SISTEMA DE APRENDIZAJE (Modal) ---
function showLearningModal() {
	const modal = document.getElementById('learning-modal');
	const question = document.getElementById('learning-question');
	const confirmation = document.getElementById('learning-confirmation');
	const submitButton = document.getElementById('submit-pokemon');
	modal.classList.remove('hidden');
	question.textContent = 'Escribe el nombre del Pokémon que pensabas.';
	confirmation.classList.add('hidden');
	submitButton.style.display = 'inline-block';
	pendingPokemon = null;
	document.getElementById('pokemon-input').focus();
}

function hideLearningModal() {
	const modal = document.getElementById('learning-modal');
	const question = document.getElementById('learning-question');
	const confirmation = document.getElementById('learning-confirmation');
	const submitButton = document.getElementById('submit-pokemon');
	modal.classList.add('hidden');
	document.getElementById('pokemon-input').value = '';
	document.getElementById('fuzzy-suggestions').classList.add('hidden');
	confirmation.classList.add('hidden');
	submitButton.style.display = 'inline-block';
	question.textContent = 'Escribe el nombre del Pokémon que pensabas.';
	pendingPokemon = null;
}

function showFuzzySuggestions(query) {
	const suggestions = [];
	for (const poke of getPokemonSearchList()) {
		const score = fuzzyMatch(query, poke);
		if (score >= 50) {
			suggestions.push({ pokemon: poke, score });
		}
	}
	
	suggestions.sort((a, b) => b.score - a.score);
	const topSuggestions = suggestions.slice(0, 5);
	
	const suggestionList = document.getElementById('suggestion-list');
	suggestionList.innerHTML = '';
	
	topSuggestions.forEach(({ pokemon, score }) => {
		const item = document.createElement('div');
		item.className = 'suggestion-item';
		item.textContent = `${capitalize(pokemon.name)} (${Math.round(score)}% similar)`;
		item.onclick = () => selectPokemon(pokemon);
		suggestionList.appendChild(item);
	});
	
	if (topSuggestions.length > 0) {
		document.getElementById('fuzzy-suggestions').classList.remove('hidden');
	}
}

async function selectPokemon(pokemon) {
	const resolvedPokemon = await ensurePokemonDetails(pokemon);
	if (!resolvedPokemon) {
		alert('No pude cargar los datos completos de ese Pokémon. Intenta de nuevo.');
		return;
	}

	// Verificar si ya está en la lista
	addPokemonToGame(resolvedPokemon);
	SFX.confirm();
	
	// Guardar en el sistema de aprendizaje
	learningSystem.learnPokemon(resolvedPokemon.id, currentSessionPath);
	
	// Mostrar confirmación
	const modal = document.getElementById('learning-modal');
	const qDiv = document.getElementById('question-text');
	qDiv.textContent = `¡Perfecto! Aprendí que tu Pokémon era ${capitalize(resolvedPokemon.name)}. 📚 Gracias por enseñarme.`;
	
	document.getElementById('yes-btn').disabled = true;
	document.getElementById('no-btn').disabled = true;
	
	// Limpiar modal después de 2 segundos
	setTimeout(() => {
		restartGame();
	}, 2000);
}

function handlePokemonSubmit() {
	const input = document.getElementById('pokemon-input').value.trim();
	if (!input) return;
	
	// Buscar con fuzzy match
	const result = findPokemonByName(input);
	if (result) {
		pendingPokemon = result.pokemon;
		document.getElementById('learning-question').textContent = `¿Era ${capitalize(result.pokemon.name)}?`;
		document.getElementById('fuzzy-suggestions').classList.add('hidden');
		document.getElementById('submit-pokemon').style.display = 'none';
		document.getElementById('learning-confirmation').classList.remove('hidden');
	} else {
		alert('No pude encontrar ese Pokémon. ¿Verificaste bien el nombre?');
	}
}

function confirmPendingPokemon() {
	if (pendingPokemon) {
		selectPokemon(pendingPokemon);
	}
}

function editPendingPokemon() {
	pendingPokemon = null;
	document.getElementById('learning-question').textContent = 'Escribe el nombre del Pokémon que pensabas.';
	document.getElementById('learning-confirmation').classList.add('hidden');
	document.getElementById('submit-pokemon').style.display = 'inline-block';
	document.getElementById('pokemon-input').focus();
}

// --- Reinicia el juego ---
function restartGame() {
	questions = buildQuestions();
	candidates = [...pokemonList];
	asked = [];
	currentQuestion = null;
	currentSessionPath = [];
	pendingGuessPokemon = null;
	awaitingGuessConfirmation = false;
	document.getElementById('question-text').textContent = "Piensa en un Pokémon y presiona 'SÍ' o 'NO' para comenzar.";
	document.getElementById('yes-btn').disabled = false;
	document.getElementById('no-btn').disabled = false;
	hideLearningModal();
	renderGrid();
}

// --- Eventos de botones ---
document.getElementById('yes-btn').onclick = () => { SFX.click(); handleAnswer(true); };
document.getElementById('no-btn').onclick = () => { SFX.click(); handleAnswer(false); };
document.getElementById('restart-btn').onclick = () => { SFX.startup(); restartGame(); };

// Eventos del modal
document.getElementById('pokemon-input').addEventListener('input', (e) => {
	const value = e.target.value.trim();
	if (value.length >= 2) {
		showFuzzySuggestions(value);
	} else {
		document.getElementById('fuzzy-suggestions').classList.add('hidden');
	}
});

document.getElementById('pokemon-input').addEventListener('keypress', (e) => {
	if (e.key === 'Enter') {
		handlePokemonSubmit();
	}
});

document.getElementById('submit-pokemon').onclick = handlePokemonSubmit;
document.getElementById('confirm-pokemon').onclick = confirmPendingPokemon;
document.getElementById('edit-pokemon').onclick = editPendingPokemon;
document.getElementById('cancel-learning').onclick = () => {
	hideLearningModal();
	restartGame();
};

// Sound toggle
const soundToggle = document.getElementById('sound-toggle');
if (soundToggle) {
	syncAudioState();
	soundToggle.onclick = () => {
		SFX.enabled = !SFX.enabled;
		syncAudioState();
	};
}

// --- Inicialización ---
window.onload = async () => {
	await loadPokemonCatalog();
	await syncStoredAddedPokemonsToGame();
	await syncLearnedPokemonsToGame();
	candidates = [...pokemonList];
	asked = [];
	currentQuestion = null;
	currentSessionPath = [];
	pendingGuessPokemon = null;
	awaitingGuessConfirmation = false;
	renderGrid();
	document.getElementById('question-text').textContent = "Piensa en un Pokémon y presiona 'SÍ' o 'NO' para comenzar.";
	document.getElementById('yes-btn').disabled = false;
	document.getElementById('no-btn').disabled = false;
	questions = buildQuestions();
	
	setTimeout(() => SFX.startup(), 300);
	
	document.addEventListener('click', () => {
		if (SFX.enabled && SFX.musicEnabled) {
			const music = document.getElementById('background-music');
			if (music && music.paused) {
				music.volume = 0.25;
				music.play().catch(() => {});
			}
		}
	});
};
