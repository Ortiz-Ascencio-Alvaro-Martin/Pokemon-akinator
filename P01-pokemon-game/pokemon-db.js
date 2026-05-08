// ===================================================================
// BASE DE DATOS EXPANDIDA DE POKÉMON (Generaciones 1-9)
// ===================================================================
// Cada Pokémon: [id, name, tipo1, tipo2, color, evoluciona, legendario, habitat, peso, altura, huevo, rareza]

const pokemonDatabase = [
	// GEN 1
	[1, "bulbasaur", "planta", "veneno", "verde", true, false, "pradera", 6.9, 0.7, "monstruo", "común"],
	[2, "ivysaur", "planta", "veneno", "verde", true, false, "pradera", 13.0, 1.0, "monstruo", "común"],
	[3, "venusaur", "planta", "veneno", "verde", false, false, "pradera", 100.0, 2.0, "monstruo", "raro"],
	[4, "charmander", "fuego", null, "naranja", true, false, "montaña", 8.5, 0.6, "monstruo", "común"],
	[5, "charmeleon", "fuego", null, "rojo", true, false, "montaña", 19.0, 1.1, "monstruo", "común"],
	[6, "charizard", "fuego", "volador", "naranja", false, false, "montaña", 90.5, 1.7, "monstruo", "raro"],
	[7, "squirtle", "agua", null, "azul", true, false, "agua", 9.0, 0.5, "agua1", "común"],
	[8, "wartortle", "agua", null, "azul", true, false, "agua", 22.5, 1.0, "agua1", "común"],
	[9, "blastoise", "agua", null, "azul", false, false, "agua", 85.5, 1.6, "agua1", "raro"],
	[10, "caterpie", "bicho", null, "verde", true, false, "bosque", 2.9, 0.3, "bicho", "común"],
	[11, "metapod", "bicho", null, "verde", true, false, "bosque", 9.9, 0.7, "bicho", "común"],
	[12, "butterfree", "bicho", "volador", "morado", false, false, "bosque", 32.0, 1.1, "bicho", "raro"],
	[25, "pikachu", "eléctrico", null, "amarillo", true, false, "bosque", 6.0, 0.4, "campo", "común"],
	[26, "raichu", "eléctrico", null, "naranja", false, false, "bosque", 30.0, 0.8, "campo", "raro"],
	[133, "eevee", "normal", null, "marrón", true, false, "ciudad", 6.5, 0.3, "campo", "común"],
	[134, "vaporeon", "agua", null, "azul", false, false, "ciudad", 29.0, 1.0, "campo", "raro"],
	[135, "jolteon", "eléctrico", null, "amarillo", false, false, "ciudad", 24.5, 0.8, "campo", "raro"],
	[136, "flareon", "fuego", null, "naranja", false, false, "ciudad", 25.0, 0.9, "campo", "raro"],
	[150, "mewtwo", "psíquico", null, "morado", false, true, "cueva", 122.0, 2.0, "legendario", "legendario"],
	[151, "mew", "psíquico", null, "rosa", false, true, "cueva", 4.0, 0.4, "legendario", "legendario"],
	// GEN 2
	[152, "chikorita", "planta", null, "verde", true, false, "pradera", 6.4, 0.9, "monstruo", "común"],
	[153, "bayleef", "planta", null, "verde", true, false, "pradera", 15.8, 1.7, "monstruo", "común"],
	[154, "meganium", "planta", null, "verde", false, false, "pradera", 100.5, 1.8, "monstruo", "raro"],
	[155, "cyndaquil", "fuego", null, "rojo", true, false, "tierra", 7.9, 0.5, "monstruo", "común"],
	[156, "quilava", "fuego", null, "rojo", true, false, "tierra", 19.0, 0.9, "monstruo", "común"],
	[157, "typhlosion", "fuego", null, "rojo", false, false, "tierra", 79.5, 1.7, "monstruo", "raro"],
	[158, "totodile", "agua", null, "azul", true, false, "agua", 9.5, 0.6, "agua1", "común"],
	[159, "croconaw", "agua", null, "azul", true, false, "agua", 25.0, 1.1, "agua1", "común"],
	[160, "feraligatr", "agua", null, "azul", false, false, "agua", 88.8, 2.3, "agua1", "raro"],
	// GEN 3
	[258, "mudkip", "agua", null, "azul", true, false, "agua", 7.6, 0.4, "agua1", "común"],
	[259, "marshtomp", "agua", "tierra", "azul", true, false, "agua", 28.0, 1.0, "agua1", "común"],
	[260, "swampert", "agua", "tierra", "azul", false, false, "agua", 81.9, 1.5, "agua1", "raro"],
	[387, "turtwig", "planta", null, "verde", true, false, "pradera", 10.2, 0.4, "monstruo", "común"],
	// GEN 4-9 (muestra representativa de ejemplos populares)
	[387, "turtwig", "planta", null, "verde", true, false, "pradera", 10.2, 0.4, "monstruo", "común"],
	[390, "chimchar", "fuego", null, "naranja", true, false, "montaña", 8.4, 0.5, "monstruo", "común"],
	[393, "piplup", "agua", null, "azul", true, false, "agua", 5.2, 0.4, "agua1", "común"],
	[439, "mime-jr", "psíquico", "hada", "rosa", true, false, "ciudad", 13.0, 0.6, "humanoide", "raro"],
	[440, "happiny", "normal", null, "rosa", true, false, "pradera", 24.4, 0.6, "amoroso", "raro"],
	[493, "arceus", "normal", null, "blanco", false, true, "cueva", 320.0, 3.2, "legendario", "legendario"],
	[494, "victini", "psíquico", "fuego", "rojo", false, true, "legendario", 4.0, 0.4, "legendario", "legendario"],
	[495, "snivy", "planta", null, "verde", true, false, "pradera", 8.9, 0.6, "monstruo", "común"],
	[496, "servine", "planta", null, "verde", true, false, "pradera", 17.3, 1.1, "monstruo", "común"],
	[497, "serperior", "planta", null, "verde", false, false, "pradera", 63.0, 2.3, "monstruo", "raro"],
	[498, "tepig", "fuego", null, "naranja", true, false, "montaña", 9.9, 0.5, "monstruo", "común"],
	[499, "pignite", "fuego", "lucha", "naranja", true, false, "montaña", 55.8, 1.0, "monstruo", "común"],
	[500, "emboar", "fuego", "lucha", "naranja", false, false, "montaña", 150.0, 1.6, "monstruo", "raro"],
	[501, "oshawott", "agua", null, "blanco", true, false, "agua", 5.9, 0.5, "agua1", "común"],
	[502, "dewott", "agua", null, "azul", true, false, "agua", 24.2, 0.8, "agua1", "común"],
	[503, "samurott", "agua", null, "azul", false, false, "agua", 94.6, 1.5, "agua1", "raro"],
	[504, "patrat", "normal", null, "marrón", true, false, "campo", 11.6, 0.5, "campo", "común"],
	[505, "watchog", "normal", null, "marrón", false, false, "campo", 27.0, 1.1, "campo", "común"],
	[506, "lillipup", "normal", null, "marrón", true, false, "campo", 4.1, 0.4, "campo", "común"],
	[507, "herdier", "normal", null, "marrón", true, false, "campo", 14.7, 0.9, "campo", "común"],
	[508, "stoutland", "normal", null, "blanco", false, false, "campo", 61.0, 1.5, "campo", "raro"],
	[650, "chespin", "planta", null, "verde", true, false, "pradera", 9.0, 0.3, "monstruo", "común"],
	[651, "quilladin", "planta", null, "verde", true, false, "pradera", 22.5, 0.8, "monstruo", "común"],
	[652, "chesnaught", "planta", "lucha", "verde", false, false, "pradera", 90.0, 1.6, "monstruo", "raro"],
	[653, "fennekin", "fuego", null, "naranja", true, false, "tierra", 9.4, 0.4, "monstruo", "común"],
	[654, "braixen", "fuego", "psíquico", "naranja", true, false, "tierra", 15.0, 1.0, "monstruo", "común"],
	[655, "delphox", "fuego", "psíquico", "naranja", false, false, "tierra", 69.0, 1.5, "monstruo", "raro"],
	[656, "froakie", "agua", null, "azul", true, false, "agua", 7.2, 0.3, "agua1", "común"],
	[657, "frogadier", "agua", null, "azul", true, false, "agua", 10.9, 0.6, "agua1", "común"],
	[658, "greninja", "agua", "siniestro", "azul", false, false, "agua", 40.0, 1.5, "agua1", "raro"],
	[722, "rowlet", "planta", "volador", "marrón", true, false, "bosque", 2.2, 0.3, "volador", "común"],
	[723, "dartrix", "planta", "volador", "marrón", true, false, "bosque", 16.0, 0.7, "volador", "común"],
	[724, "decidueye", "planta", "fantasma", "marrón", false, false, "bosque", 36.3, 1.6, "volador", "raro"],
	[725, "litten", "fuego", null, "naranja", true, false, "tierra", 4.3, 0.4, "monstruo", "común"],
	[726, "torracat", "fuego", null, "naranja", true, false, "tierra", 25.0, 0.7, "monstruo", "común"],
	[727, "incineroar", "fuego", "siniestro", "naranja", false, false, "tierra", 83.0, 1.8, "monstruo", "raro"],
	[728, "popplio", "agua", null, "azul", true, false, "agua", 7.5, 0.4, "agua1", "común"],
	[729, "brionne", "agua", null, "azul", true, false, "agua", 17.5, 0.6, "agua1", "común"],
	[730, "primarina", "agua", "hada", "azul", false, false, "agua", 44.0, 1.8, "agua1", "raro"],
	[906, "sprigatito", "planta", null, "verde", true, false, "pradera", 2.4, 0.3, "monstruo", "común"],
	[907, "floragato", "planta", null, "verde", true, false, "pradera", 14.0, 0.9, "monstruo", "común"],
	[908, "meowscarada", "planta", "siniestro", "verde", false, false, "pradera", 45.0, 1.6, "monstruo", "raro"],
	[909, "fuecoco", "fuego", null, "rojo", true, false, "tierra", 9.8, 0.4, "monstruo", "común"],
	[910, "crocalor", "fuego", null, "rojo", true, false, "tierra", 25.0, 1.0, "monstruo", "común"],
	[911, "skeledirge", "fuego", "fantasma", "rojo", false, false, "tierra", 56.0, 1.6, "monstruo", "raro"],
	[912, "quaxly", "agua", null, "azul", true, false, "agua", 6.5, 0.5, "agua1", "común"],
	[913, "quaxwell", "agua", null, "azul", true, false, "agua", 26.5, 1.0, "agua1", "común"],
	[914, "quaquaval", "agua", "lucha", "azul", false, false, "agua", 55.0, 1.7, "agua1", "raro"]
];

// Convertir a objetos con propiedades
function pokemonToObject([id, name, tipo1, tipo2, color, evoluciona, legendario, habitat, peso, altura, huevo, rareza]) {
	return { id, name, tipo1, tipo2, color, evoluciona, legendario, habitat, peso, altura, huevo, rareza };
}

const fullPokemonList = pokemonDatabase.map(pokemonToObject);

// Catálogo completo de nombres de Pokémon para búsqueda/aprendizaje.
// El juego visible sigue arrancando con la lista pequeña, pero aquí están todos.
let pokemonCatalog = [];
let pokemonCatalogLoaded = false;

const pokemonCatalogCacheKey = 'pokemonCatalogCache_v1';
const pokemonDetailCacheKey = 'pokemonDetailCache_v1';
const pokemonApiBase = 'https://pokeapi.co/api/v2';

function normalizeSearchText(value) {
	return String(value || '')
		.toLowerCase()
		.normalize('NFD')
		.replace(/[\u0300-\u036f]/g, '');
}

function extractPokemonId(url) {
	const match = String(url || '').match(/\/pokemon\/(\d+)\/?$/);
	return match ? Number(match[1]) : null;
}

function translateType(apiType) {
	const typeMap = {
		normal: 'normal',
		fighting: 'lucha',
		flying: 'volador',
		poison: 'veneno',
		ground: 'tierra',
		rock: 'roca',
		bug: 'bicho',
		ghost: 'fantasma',
		steel: 'acero',
		fire: 'fuego',
		water: 'agua',
		grass: 'planta',
		electric: 'eléctrico',
		psychic: 'psíquico',
		ice: 'hielo',
		dragon: 'dragón',
		dark: 'siniestro',
		fairy: 'hada'
	};

	return typeMap[apiType] || apiType || 'normal';
}

function translateColor(apiColor) {
	const colorMap = {
		black: 'negro',
		blue: 'azul',
		brown: 'marrón',
		gray: 'gris',
		green: 'verde',
		pink: 'rosa',
		purple: 'morado',
		red: 'rojo',
		white: 'blanco',
		yellow: 'amarillo'
	};

	return colorMap[apiColor] || apiColor || 'blanco';
}

function translateHabitat(apiHabitat) {
	const habitatMap = {
		cave: 'cueva',
		forest: 'bosque',
		grassland: 'pradera',
		mountain: 'montaña',
		rare: 'raro',
		'rough-terrain': 'terreno',
		sea: 'mar',
		urban: 'ciudad',
		'waters-edge': 'agua'
	};

	return habitatMap[apiHabitat] || apiHabitat || 'desconocido';
}

function translateEggGroup(apiEggGroup) {
	const eggGroupMap = {
		monster: 'monstruo',
		water1: 'agua1',
		water2: 'agua2',
		water3: 'agua3',
		bug: 'bicho',
		flying: 'volador',
		field: 'campo',
		fairy: 'hada',
		grass: 'planta',
		'human-like': 'humanoide',
		mineral: 'mineral',
		amorphous: 'amoroso',
		dragon: 'dragón',
		ditto: 'ditto',
		undiscovered: 'desconocido',
		'no-eggs': 'sin-huevo'
	};

	return eggGroupMap[apiEggGroup] || apiEggGroup || 'desconocido';
}

function findEvolutionNode(chainNode, speciesName) {
	if (!chainNode) return null;
	if (normalizeSearchText(chainNode.species?.name) === normalizeSearchText(speciesName)) {
		return chainNode;
	}

	for (const nextNode of chainNode.evolves_to || []) {
		const found = findEvolutionNode(nextNode, speciesName);
		if (found) return found;
	}

	return null;
}

function buildPokemonFromApi(pokemonData, speciesData, evolutionChainData) {
	const types = (pokemonData.types || [])
		.map(entry => translateType(entry.type?.name))
		.filter(Boolean);
	const eggGroups = (speciesData.egg_groups || [])
		.map(entry => translateEggGroup(entry.name))
		.filter(Boolean);
	const evolutionNode = evolutionChainData
		? findEvolutionNode(evolutionChainData.chain, speciesData.name)
		: null;
	const evoluciona = Boolean(evolutionNode && (evolutionNode.evolves_to || []).length > 0);
	const legendario = Boolean(speciesData.is_legendary || speciesData.is_mythical);

	return {
		id: pokemonData.id,
		name: pokemonData.name,
		tipo1: types[0] || 'normal',
		tipo2: types[1] || null,
		color: translateColor(speciesData.color?.name),
		evoluciona,
		legendario,
		habitat: translateHabitat(speciesData.habitat?.name),
		peso: Number(((pokemonData.weight || 0) / 10).toFixed(1)),
		altura: Number(((pokemonData.height || 0) / 10).toFixed(1)),
		huevo: eggGroups[0] || 'desconocido',
		rareza: legendario ? 'legendario' : (evoluciona ? 'común' : 'raro')
	};
}

function getCachedPokemonDetails() {
	try {
		const raw = localStorage.getItem(pokemonDetailCacheKey);
		return raw ? JSON.parse(raw) : {};
	} catch (e) {
		return {};
	}
}

function saveCachedPokemonDetails(cache) {
	try {
		localStorage.setItem(pokemonDetailCacheKey, JSON.stringify(cache));
	} catch (e) {
		console.error('Error saving pokemon detail cache:', e);
	}
}

function getPokemonSearchList() {
	return pokemonCatalogLoaded && pokemonCatalog.length > 0 ? pokemonCatalog : fullPokemonList;
}

async function loadPokemonCatalog() {
	if (pokemonCatalogLoaded && pokemonCatalog.length > 0) {
		return pokemonCatalog;
	}

	try {
		const cached = localStorage.getItem(pokemonCatalogCacheKey);
		if (cached) {
			pokemonCatalog = JSON.parse(cached);
			pokemonCatalogLoaded = true;
			return pokemonCatalog;
		}
	} catch (e) {
		console.error('Error loading pokemon catalog cache:', e);
	}

	try {
		const response = await fetch(`${pokemonApiBase}/pokemon?limit=2000`);
		if (!response.ok) {
			throw new Error(`Catalog request failed with status ${response.status}`);
		}

		const data = await response.json();
		pokemonCatalog = (data.results || [])
			.map(item => ({
				id: extractPokemonId(item.url),
				name: item.name,
				url: item.url
			}))
			.filter(item => item.id);
		pokemonCatalogLoaded = true;

		try {
			localStorage.setItem(pokemonCatalogCacheKey, JSON.stringify(pokemonCatalog));
		} catch (e) {
			console.error('Error saving pokemon catalog cache:', e);
		}

		return pokemonCatalog;
	} catch (e) {
		console.error('Error loading pokemon catalog:', e);
		pokemonCatalog = fullPokemonList.map(p => ({ id: p.id, name: p.name, url: `${pokemonApiBase}/pokemon/${p.id}/` }));
		pokemonCatalogLoaded = false;
		return pokemonCatalog;
	}
}

async function loadPokemonDetails(pokemonIdentifier) {
	const id = typeof pokemonIdentifier === 'number'
		? pokemonIdentifier
		: Number(pokemonIdentifier?.id || extractPokemonId(pokemonIdentifier?.url));

	if (!id) return null;

	const existing = fullPokemonList.find(p => p.id === id && p.tipo1);
	if (existing) {
		return { ...existing };
	}

	const cachedDetails = getCachedPokemonDetails();
	if (cachedDetails[String(id)]) {
		return { ...cachedDetails[String(id)] };
	}

	try {
		const pokemonResponse = await fetch(`${pokemonApiBase}/pokemon/${id}/`);
		if (!pokemonResponse.ok) {
			throw new Error(`Pokemon request failed with status ${pokemonResponse.status}`);
		}
		const pokemonData = await pokemonResponse.json();

		const speciesResponse = await fetch(pokemonData.species.url);
		if (!speciesResponse.ok) {
			throw new Error(`Species request failed with status ${speciesResponse.status}`);
		}
		const speciesData = await speciesResponse.json();

		let evolutionChainData = null;
		if (speciesData.evolution_chain?.url) {
			const evolutionResponse = await fetch(speciesData.evolution_chain.url);
			if (evolutionResponse.ok) {
				evolutionChainData = await evolutionResponse.json();
			}
		}

		const pokemon = buildPokemonFromApi(pokemonData, speciesData, evolutionChainData);
		cachedDetails[String(id)] = pokemon;
		saveCachedPokemonDetails(cachedDetails);
		return pokemon;
	} catch (e) {
		console.error(`Error loading details for pokemon ${id}:`, e);
		return null;
	}
}

async function ensurePokemonDetails(pokemon) {
	if (!pokemon) return null;
	if (pokemon.tipo1) return { ...pokemon };
	return loadPokemonDetails(pokemon);
}

// ===================================================================
// SISTEMA DE BÚSQUEDA DIFUSA (Fuzzy Matching)
// ===================================================================

function levenshteinDistance(a, b) {
	const matrix = [];
	for (let i = 0; i <= b.length; i++) {
		matrix[i] = [i];
	}
	for (let j = 0; j <= a.length; j++) {
		matrix[0][j] = j;
	}
	for (let i = 1; i <= b.length; i++) {
		for (let j = 1; j <= a.length; j++) {
			if (b.charAt(i - 1) === a.charAt(j - 1)) {
				matrix[i][j] = matrix[i - 1][j - 1];
			} else {
				matrix[i][j] = Math.min(
					matrix[i - 1][j - 1] + 1,
					matrix[i][j - 1] + 1,
					matrix[i - 1][j] + 1
				);
			}
		}
	}
	return matrix[b.length][a.length];
}

function fuzzyMatch(query, pokemon) {
	const name = normalizeSearchText(pokemon.name);
	const q = normalizeSearchText(query).trim();
	
	// Match exacto
	if (name === q) return 100;
	if (name.includes(q)) return 90;
	
	// Levenshtein distance (normalizado)
	const distance = levenshteinDistance(q, name);
	const maxLen = Math.max(q.length, name.length);
	const similarity = Math.max(0, 100 - (distance / maxLen) * 100);
	
	return similarity;
}

function findPokemonByName(query) {
	let best = null;
	let bestScore = -Infinity;
	const searchList = getPokemonSearchList();
	
	for (const pokemon of searchList) {
		const score = fuzzyMatch(query, pokemon);
		if (score > bestScore) {
			bestScore = score;
			best = pokemon;
		}
	}
	
	// Solo retornar si la similitud es >= 60%
	return bestScore >= 60 ? { pokemon: best, score: bestScore } : null;
}

// ===================================================================
// SISTEMA DE APRENDIZAJE
// ===================================================================

class PokemonLearningSystem {
	constructor() {
		this.learnedData = this.loadLearningData();
		this.currentSession = [];
	}
	
	// Guardar una ruta de decisión que llevó a un Pokémon
	learnPokemon(pokemonId, questionPath) {
		if (!this.learnedData[pokemonId]) {
			this.learnedData[pokemonId] = {
				id: pokemonId,
				paths: [],
				frequency: 0
			};
		}
		
		this.learnedData[pokemonId].paths.push({
			questions: questionPath,
			timestamp: Date.now()
		});
		
		this.learnedData[pokemonId].frequency++;
		this.saveLearningData();
	}
	
	// Obtener Pokémon que no están en la lista del juego
	getUnplayedPokemons(playedList) {
		const playedIds = new Set(playedList.map(p => p.id));
		return fullPokemonList.filter(p => !playedIds.has(p.id));
	}
	
	saveLearningData() {
		try {
			localStorage.setItem('pokemonLearning', JSON.stringify(this.learnedData));
		} catch (e) {
			console.error('Error saving learning data:', e);
		}
	}
	
	loadLearningData() {
		try {
			const data = localStorage.getItem('pokemonLearning');
			return data ? JSON.parse(data) : {};
		} catch (e) {
			console.error('Error loading learning data:', e);
			return {};
		}
	}
	
	// Sugerir un Pokémon de la BD completa
	suggestRandomUnplayed(playedList) {
		const unplayed = this.getUnplayedPokemons(playedList);
		if (unplayed.length === 0) return null;
		return unplayed[Math.floor(Math.random() * unplayed.length)];
	}
}

// ===================================================================
// EXPORTAR PARA USO EN script.js
// ===================================================================
