
// --- Base de datos de Pokémon Gen 1 (151) ---

// id, name, tipo1, tipo2, color, evoluciona, legendario, habitat, peso, altura, huevo, rareza
const kantoData = [
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
	[13, "weedle", "bicho", "veneno", "amarillo", true, false, "bosque", 3.2, 0.3, "bicho", "común"],
	[14, "kakuna", "bicho", "veneno", "amarillo", true, false, "bosque", 10.0, 0.6, "bicho", "común"],
	[15, "beedrill", "bicho", "veneno", "amarillo", false, false, "bosque", 29.5, 1.0, "bicho", "raro"],
	[16, "pidgey", "normal", "volador", "marrón", true, false, "pradera", 1.8, 0.3, "volador", "común"],
	[17, "pidgeotto", "normal", "volador", "marrón", true, false, "pradera", 30.0, 1.1, "volador", "común"],
	[18, "pidgeot", "normal", "volador", "marrón", false, false, "pradera", 39.5, 1.5, "volador", "raro"],
	[19, "rattata", "normal", null, "morado", true, false, "pradera", 3.5, 0.3, "campo", "común"],
	[20, "raticate", "normal", null, "marrón", false, false, "pradera", 18.5, 0.7, "campo", "común"],
	[21, "spearow", "normal", "volador", "marrón", true, false, "pradera", 2.0, 0.3, "volador", "común"],
	[22, "fearow", "normal", "volador", "marrón", false, false, "pradera", 38.0, 1.2, "volador", "común"],
	[23, "ekans", "veneno", null, "morado", true, false, "cueva", 6.9, 2.0, "campo", "común"],
	[24, "arbok", "veneno", null, "morado", false, false, "cueva", 65.0, 3.5, "campo", "común"],
	[25, "pikachu", "eléctrico", null, "amarillo", true, false, "bosque", 6.0, 0.4, "campo", "común"],
	[26, "raichu", "eléctrico", null, "naranja", false, false, "bosque", 30.0, 0.8, "campo", "raro"],
	[27, "sandshrew", "tierra", null, "amarillo", true, false, "desierto", 12.0, 0.6, "campo", "común"],
	[28, "sandslash", "tierra", null, "amarillo", false, false, "desierto", 29.5, 1.0, "campo", "común"],
	[29, "nidoran-f", "veneno", null, "rosa", true, false, "pradera", 7.0, 0.4, "monstruo", "común"],
	[30, "nidorina", "veneno", null, "azul", true, false, "pradera", 20.0, 0.8, "monstruo", "común"],
	[31, "nidoqueen", "veneno", "tierra", "azul", false, false, "pradera", 60.0, 1.3, "monstruo", "raro"],
	[32, "nidoran-m", "veneno", null, "morado", true, false, "pradera", 9.0, 0.5, "monstruo", "común"],
	[33, "nidorino", "veneno", null, "morado", true, false, "pradera", 19.5, 0.9, "monstruo", "común"],
	[34, "nidoking", "veneno", "tierra", "morado", false, false, "pradera", 62.0, 1.4, "monstruo", "raro"],
	[35, "clefairy", "hada", null, "rosa", true, false, "cueva", 7.5, 0.6, "hada", "común"],
	[36, "clefable", "hada", null, "rosa", false, false, "cueva", 40.0, 1.3, "hada", "raro"],
	[37, "vulpix", "fuego", null, "naranja", true, false, "pradera", 9.9, 0.6, "campo", "común"],
	[38, "ninetales", "fuego", null, "naranja", false, false, "pradera", 19.9, 1.1, "campo", "raro"],
	[39, "jigglypuff", "normal", "hada", "rosa", true, false, "pradera", 5.5, 0.5, "hada", "común"],
	[40, "wigglytuff", "normal", "hada", "rosa", false, false, "pradera", 12.0, 1.0, "hada", "raro"],
	[41, "zubat", "veneno", "volador", "azul", true, false, "cueva", 7.5, 0.8, "volador", "común"],
	[42, "golbat", "veneno", "volador", "azul", true, false, "cueva", 55.0, 1.6, "volador", "común"],
	[43, "oddish", "planta", "veneno", "azul", true, false, "pradera", 5.4, 0.5, "planta", "común"],
	[44, "gloom", "planta", "veneno", "azul", true, false, "pradera", 8.6, 0.8, "planta", "común"],
	[45, "vileplume", "planta", "veneno", "azul", false, false, "pradera", 18.6, 1.2, "planta", "raro"],
	[46, "paras", "bicho", "planta", "naranja", true, false, "bosque", 5.4, 0.3, "bicho", "común"],
	[47, "parasect", "bicho", "planta", "rojo", false, false, "bosque", 29.5, 1.0, "bicho", "raro"],
	[48, "venonat", "bicho", "veneno", "morado", true, false, "bosque", 30.0, 1.0, "bicho", "común"],
	[49, "venomoth", "bicho", "veneno", "morado", false, false, "bosque", 12.5, 1.5, "bicho", "raro"],
	[50, "diglett", "tierra", null, "marrón", true, false, "cueva", 0.8, 0.2, "campo", "común"],
	[51, "dugtrio", "tierra", null, "marrón", false, false, "cueva", 33.3, 0.7, "campo", "común"],
	[52, "meowth", "normal", null, "crema", true, false, "ciudad", 4.2, 0.4, "campo", "común"],
	[53, "persian", "normal", null, "crema", false, false, "ciudad", 32.0, 1.0, "campo", "raro"],
	[54, "psyduck", "agua", null, "amarillo", true, false, "agua", 19.6, 0.8, "agua1", "común"],
	[55, "golduck", "agua", null, "azul", false, false, "agua", 76.6, 1.7, "agua1", "raro"],
	[56, "mankey", "lucha", null, "crema", true, false, "montaña", 28.0, 0.5, "campo", "común"],
	[57, "primeape", "lucha", null, "crema", false, false, "montaña", 32.0, 1.0, "campo", "común"],
	[58, "growlithe", "fuego", null, "naranja", true, false, "pradera", 19.0, 0.7, "campo", "común"],
	[59, "arcanine", "fuego", null, "naranja", false, false, "pradera", 155.0, 1.9, "campo", "raro"],
	[60, "poliwag", "agua", null, "azul", true, false, "agua", 12.4, 0.6, "agua1", "común"],
	[61, "poliwhirl", "agua", null, "azul", true, false, "agua", 20.0, 1.0, "agua1", "común"],
	[62, "poliwrath", "agua", "lucha", "azul", false, false, "agua", 54.0, 1.3, "agua1", "raro"],
	[63, "abra", "psíquico", null, "amarillo", true, false, "cueva", 19.5, 0.9, "campo", "común"],
	[64, "kadabra", "psíquico", null, "amarillo", true, false, "cueva", 56.5, 1.3, "campo", "común"],
	[65, "alakazam", "psíquico", null, "amarillo", false, false, "cueva", 48.0, 1.5, "campo", "raro"],
	[66, "machop", "lucha", null, "gris", true, false, "cueva", 19.5, 0.8, "campo", "común"],
	[67, "machoke", "lucha", null, "gris", true, false, "cueva", 70.5, 1.5, "campo", "común"],
	[68, "machamp", "lucha", null, "gris", false, false, "cueva", 130.0, 1.6, "campo", "raro"],
	[69, "bellsprout", "planta", "veneno", "verde", true, false, "pradera", 4.0, 0.7, "planta", "común"],
	[70, "weepinbell", "planta", "veneno", "verde", true, false, "pradera", 6.4, 1.0, "planta", "común"],
	[71, "victreebel", "planta", "veneno", "verde", false, false, "pradera", 15.5, 1.7, "planta", "raro"],
	[72, "tentacool", "agua", "veneno", "azul", true, false, "agua", 45.5, 0.9, "agua1", "común"],
	[73, "tentacruel", "agua", "veneno", "azul", false, false, "agua", 55.0, 1.6, "agua1", "raro"],
	[74, "geodude", "roca", "tierra", "gris", true, false, "montaña", 20.0, 0.4, "tierra", "común"],
	[75, "graveler", "roca", "tierra", "gris", true, false, "montaña", 105.0, 1.0, "tierra", "común"],
	[76, "golem", "roca", "tierra", "gris", false, false, "montaña", 300.0, 1.4, "tierra", "raro"],
	[77, "ponyta", "fuego", null, "naranja", true, false, "pradera", 30.0, 1.0, "campo", "común"],
	[78, "rapidash", "fuego", null, "naranja", false, false, "pradera", 95.0, 1.7, "campo", "raro"],
	[79, "slowpoke", "agua", "psíquico", "rosa", true, false, "agua", 36.0, 1.2, "agua1", "común"],
	[80, "slowbro", "agua", "psíquico", "rosa", false, false, "agua", 78.5, 1.6, "agua1", "raro"],
	[81, "magnemite", "eléctrico", "acero", "gris", true, false, "planta", 6.0, 0.3, "amorphous", "común"],
	[82, "magneton", "eléctrico", "acero", "gris", false, false, "planta", 60.0, 1.0, "amorphous", "común"],
	[83, "farfetchd", "normal", "volador", "marrón", false, false, "pradera", 15.0, 0.8, "volador", "raro"],
	[84, "doduo", "normal", "volador", "marrón", true, false, "pradera", 39.2, 1.4, "volador", "común"],
	[85, "dodrio", "normal", "volador", "marrón", false, false, "pradera", 85.2, 1.8, "volador", "raro"],
	[86, "seel", "agua", "hielo", "blanco", true, false, "agua", 90.0, 1.1, "agua1", "común"],
	[87, "dewgong", "agua", "hielo", "blanco", false, false, "agua", 120.0, 1.7, "agua1", "raro"],
	[88, "grimer", "veneno", null, "morado", true, false, "ciudad", 30.0, 0.9, "amorphous", "común"],
	[89, "muk", "veneno", null, "morado", false, false, "ciudad", 30.0, 1.2, "amorphous", "raro"],
	[90, "shellder", "agua", null, "morado", true, false, "agua", 4.0, 0.3, "agua1", "común"],
	[91, "cloyster", "agua", "hielo", "morado", false, false, "agua", 132.5, 1.6, "agua1", "raro"],
	[92, "gastly", "fantasma", "veneno", "morado", true, false, "torre", 0.1, 1.3, "amorphous", "común"],
	[93, "haunter", "fantasma", "veneno", "morado", true, false, "torre", 0.1, 1.6, "amorphous", "común"],
	[94, "gengar", "fantasma", "veneno", "morado", false, false, "torre", 40.5, 1.5, "amorphous", "raro"],
	[95, "onix", "roca", "tierra", "gris", false, false, "cueva", 210.0, 8.8, "roca", "raro"],
	[96, "drowzee", "psíquico", null, "amarillo", true, false, "pradera", 32.4, 1.0, "campo", "común"],
	[97, "hypno", "psíquico", null, "amarillo", false, false, "pradera", 75.6, 1.6, "campo", "raro"],
	[98, "krabby", "agua", null, "naranja", true, false, "agua", 6.5, 0.4, "agua1", "común"],
	[99, "kingler", "agua", null, "naranja", false, false, "agua", 60.0, 1.3, "agua1", "raro"],
	[100, "voltorb", "eléctrico", null, "rojo", true, false, "planta", 10.4, 0.5, "amorphous", "común"],
	[101, "electrode", "eléctrico", null, "rojo", false, false, "planta", 66.6, 1.2, "amorphous", "común"],
	[102, "exeggcute", "planta", "psíquico", "rosa", true, false, "pradera", 2.5, 0.4, "planta", "común"],
	[103, "exeggutor", "planta", "psíquico", "verde", false, false, "pradera", 120.0, 2.0, "planta", "raro"],
	[104, "cubone", "tierra", null, "marrón", true, false, "cueva", 6.5, 0.4, "campo", "común"],
	[105, "marowak", "tierra", null, "marrón", false, false, "cueva", 45.0, 1.0, "campo", "raro"],
	[106, "hitmonlee", "lucha", null, "marrón", false, false, "ciudad", 49.8, 1.5, "campo", "raro"],
	[107, "hitmonchan", "lucha", null, "marrón", false, false, "ciudad", 50.2, 1.4, "campo", "raro"],
	[108, "lickitung", "normal", null, "rosa", false, false, "pradera", 65.5, 1.2, "campo", "raro"],
	[109, "koffing", "veneno", null, "morado", true, false, "cueva", 1.0, 0.6, "amorphous", "común"],
	[110, "weezing", "veneno", null, "morado", false, false, "cueva", 9.5, 1.2, "amorphous", "raro"],
	[111, "rhyhorn", "tierra", "roca", "gris", true, false, "cueva", 115.0, 1.0, "roca", "común"],
	[112, "rhydon", "tierra", "roca", "gris", false, false, "cueva", 120.0, 1.9, "roca", "raro"],
	[113, "chansey", "normal", null, "rosa", false, false, "pradera", 34.6, 1.1, "amoroso", "raro"],
	[114, "tangela", "planta", null, "azul", false, false, "pradera", 35.0, 1.0, "planta", "raro"],
	[115, "kangaskhan", "normal", null, "marrón", false, false, "pradera", 80.0, 2.2, "campo", "raro"],
	[116, "horsea", "agua", null, "azul", true, false, "agua", 8.0, 0.4, "agua1", "común"],
	[117, "seadra", "agua", null, "azul", false, false, "agua", 25.0, 1.2, "agua1", "común"],
	[118, "goldeen", "agua", null, "rojo", true, false, "agua", 15.0, 0.6, "agua1", "común"],
	[119, "seaking", "agua", null, "rojo", false, false, "agua", 39.0, 1.3, "agua1", "común"],
	[120, "staryu", "agua", null, "marrón", true, false, "agua", 34.5, 0.8, "agua1", "común"],
	[121, "starmie", "agua", "psíquico", "morado", false, false, "agua", 80.0, 1.1, "agua1", "raro"],
	[122, "mr-mime", "psíquico", "hada", "rosa", false, false, "ciudad", 54.0, 1.3, "humanoide", "raro"],
	[123, "scyther", "bicho", "volador", "verde", false, false, "bosque", 56.0, 1.5, "bicho", "raro"],
	[124, "jynx", "hielo", "psíquico", "rosa", false, false, "cueva", 40.6, 1.4, "humanoide", "raro"],
	[125, "electabuzz", "eléctrico", null, "amarillo", false, false, "planta", 30.0, 1.1, "humanoide", "raro"],
	[126, "magmar", "fuego", null, "rojo", false, false, "cueva", 44.5, 1.3, "humanoide", "raro"],
	[127, "pinsir", "bicho", null, "marrón", false, false, "bosque", 55.0, 1.5, "bicho", "raro"],
	[128, "tauros", "normal", null, "marrón", false, false, "pradera", 88.4, 1.4, "campo", "raro"],
	[129, "magikarp", "agua", null, "naranja", true, false, "agua", 10.0, 0.9, "agua1", "común"],
	[130, "gyarados", "agua", "volador", "azul", false, false, "agua", 235.0, 6.5, "agua1", "raro"],
	[131, "lapras", "agua", "hielo", "azul", false, false, "agua", 220.0, 2.5, "agua1", "raro"],
	[132, "ditto", "normal", null, "morado", false, false, "ciudad", 4.0, 0.3, "amoroso", "raro"],
	[133, "eevee", "normal", null, "marrón", true, false, "ciudad", 6.5, 0.3, "campo", "común"],
	[134, "vaporeon", "agua", null, "azul", false, false, "ciudad", 29.0, 1.0, "campo", "raro"],
	[135, "jolteon", "eléctrico", null, "amarillo", false, false, "ciudad", 24.5, 0.8, "campo", "raro"],
	[136, "flareon", "fuego", null, "naranja", false, false, "ciudad", 25.0, 0.9, "campo", "raro"],
	[137, "porygon", "normal", null, "rosa", false, false, "ciudad", 36.5, 0.8, "amorphous", "raro"],
	[138, "omanyte", "roca", "agua", "azul", true, false, "cueva", 7.5, 0.4, "agua1", "común"],
	[139, "omastar", "roca", "agua", "azul", false, false, "cueva", 35.0, 1.0, "agua1", "raro"],
	[140, "kabuto", "roca", "agua", "marrón", true, false, "cueva", 11.5, 0.5, "agua1", "común"],
	[141, "kabutops", "roca", "agua", "marrón", false, false, "cueva", 40.5, 1.3, "agua1", "raro"],
	[142, "aerodactyl", "roca", "volador", "morado", false, false, "cueva", 59.0, 1.8, "fósil", "raro"],
	[143, "snorlax", "normal", null, "azul", false, false, "pradera", 460.0, 2.1, "campo", "raro"],
	[144, "articuno", "hielo", "volador", "azul", false, true, "cielo", 55.4, 1.7, "legendario", "legendario"],
	[145, "zapdos", "eléctrico", "volador", "amarillo", false, true, "cielo", 52.6, 1.6, "legendario", "legendario"],
	[146, "moltres", "fuego", "volador", "naranja", false, true, "cielo", 60.0, 2.0, "legendario", "legendario"],
	[147, "dratini", "dragón", null, "azul", true, false, "agua", 3.3, 1.8, "agua1", "común"],
	[148, "dragonair", "dragón", null, "azul", true, false, "agua", 16.5, 4.0, "agua1", "raro"],
	[149, "dragonite", "dragón", "volador", "naranja", false, false, "agua", 210.0, 2.2, "agua1", "raro"],
	[150, "mewtwo", "psíquico", null, "morado", false, true, "cueva", 122.0, 2.0, "legendario", "legendario"],
	[151, "mew", "psíquico", null, "rosa", false, true, "cueva", 4.0, 0.4, "legendario", "legendario"]
];

const pokemonList = kantoData.map(([id, name, tipo1, tipo2, color, evoluciona, legendario, habitat, peso, altura, huevo, rareza]) => ({
	id, name, tipo1, tipo2, color, evoluciona, legendario, habitat, peso, altura, huevo, rareza
}));

// --- Preguntas posibles (generadas desde los atributos) ---
let questions = [];

function capitalize(s){ return String(s).charAt(0).toUpperCase() + String(s).slice(1); }

function buildQuestions() {
	const qs = [];
	
	// 1️⃣ PREGUNTAS DIVERTIDAS Y COMUNES (prioritario)
	qs.push({ key: 'legendario', value: true, text: '¿Es legendario?' });
	qs.push({ key: 'evoluciona', value: true, text: '¿Puede evolucionar?' });

	// 2️⃣ PREGUNTAS SOBRE TIPOS (muy populares y divertidas)
	const tipos = new Set();
	pokemonList.forEach(p => { if(p.tipo1) tipos.add(p.tipo1); if(p.tipo2) tipos.add(p.tipo2); });
	
	// Ordenar tipos por popularidad/diversión: agua, fuego, planta, eléctrico, psíquico, etc.
	const tiposOrdenados = ['agua', 'fuego', 'planta', 'normal', 'eléctrico', 'psíquico', 'hielo', 'roca', 
							'tierra', 'volador', 'bicho', 'veneno', 'lucha', 'dragón', 'fantasma', 'acero', 'hada'];
	
	tiposOrdenados.forEach(t => {
		if (tipos.has(t)) {
			qs.push({ key: 'tipo1', value: t, text: `¿Es de tipo ${capitalize(t)}?` });
		}
	});
	
	// Agregar tipos secundarios (también comunes pero menos prioritarios)
	tiposOrdenados.forEach(t => {
		if (tipos.has(t)) {
			qs.push({ key: 'tipo2', value: t, text: `¿Tiene tipo ${capitalize(t)}?` });
		}
	});

	// 3️⃣ PREGUNTAS SOBRE COLORES (divertidas y fáciles de imaginar)
	const colors = new Set(pokemonList.map(p => p.color).filter(Boolean));
	const coloresOrdenados = ['azul', 'rojo', 'verde', 'amarillo', 'naranja', 'rosa', 'morado', 'marrón', 
							   'gris', 'blanco', 'crema', 'negro'];
	
	coloresOrdenados.forEach(c => {
		if (colors.has(c)) {
			qs.push({ key: 'color', value: c, text: `¿Es de color ${capitalize(c)}?` });
		}
	});

	// 4️⃣ PREGUNTAS SOBRE HÁBITATS (comunes)
	const habitats = new Set(pokemonList.map(p => p.habitat).filter(Boolean));
	habitats.forEach(h => qs.push({ key: 'habitat', value: h, text: `¿Vive en ${capitalize(h)}?` }));

	// 5️⃣ PREGUNTAS SOBRE RAREZA
	const rares = new Set(pokemonList.map(p => p.rareza).filter(Boolean));
	rares.forEach(r => qs.push({ key: 'rareza', value: r, text: `¿Es ${r} (rareza)?` }));

	// 6️⃣ PREGUNTAS SOBRE GRUPOS DE HUEVO (más específicas)
	const eggs = new Set(pokemonList.map(p => p.huevo).filter(Boolean));
	eggs.forEach(e => qs.push({ key: 'huevo', value: e, text: `¿Pertenece al grupo huevo ${capitalize(e)}?` }));

	// 7️⃣ PREGUNTAS SOBRE PESO Y ALTURA (más específicas)
	const pesoThresholds = [1, 5, 10, 20, 50, 100];
	pesoThresholds.forEach(th => qs.push({ key: 'peso', value: v => (v || 0) > th, text: `¿Pesa más de ${th}kg?` }));
	
	const alturaThresholds = [0.5, 1.0, 1.5, 2.0];
	alturaThresholds.forEach(th => qs.push({ key: 'altura', value: v => (v || 0) > th, text: `¿Mide más de ${th}m?` }));

	return qs;
}

questions = buildQuestions();

// --- Heurística: elegir la pregunta que mejor divide (más balanceada) ---
function pickBestQuestion() {
	// Prefer the question with highest entropy (most balanced split)
	function entropy(p) {
		if (p <= 0 || p >= 1) return 0;
		return - (p * Math.log2(p) + (1 - p) * Math.log2(1 - p));
	}

	let best = null;
	let bestScore = -Infinity; // we want max entropy
	for (const q of questions) {
		if (asked.includes(q.text)) continue;
		let yesCount = 0, noCount = 0, undefinedCount = 0;
		for (const pk of candidates) {
			let yes = false;
			if (typeof q.value === 'function') {
				try { yes = q.value(pk[q.key]); } catch (e) { yes = false; }
			} else {
				// treat undefined attribute as not matching
				if (pk[q.key] === undefined) { undefinedCount++; yes = false; }
				else yes = pk[q.key] === q.value;
			}
			if (yes) yesCount++; else noCount++;
		}
		const total = yesCount + noCount;
		if (total === 0) continue;
		if (yesCount === 0 || noCount === 0) continue; // skip trivial splits

		const p = yesCount / total;
		const qEntropy = entropy(p);

		// priority index: preguntas que aparecen primero en la lista tienen más prioridad
		const qIndex = questions.indexOf(q);
		// tie-breaker: prefer questions by priority order, then entropy, then candidate count
		const score = (1 / (qIndex + 1)) + qEntropy * 0.5 + Math.log2(total + 1) * 0.01;

		if (score > bestScore) {
			bestScore = score;
			best = q;
		}
	}
	return best;
}

// --- Estado del juego ---
let candidates = [];
let asked = [];
let currentQuestion = null;

// --- Simple SFX usando WebAudio ---
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

			this.musicGain = this.ctx.createGain();
			this.musicGain.gain.value = 0.15;
			this.musicGain.connect(this.ctx.destination);
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
		} catch (e) { /* ignore audio errors */ }
	},

	// 8-bit style retro sounds
	click() { 
		this.playTone(900, 40); 
	},
	
	confirm() { 
		this.playTone(520, 160); 
		setTimeout(() => this.playTone(720, 120), 150); 
	},

	hover() {
		this.playTone(1200, 25);
	},

	select() {
		this.playTone(600, 80);
		setTimeout(() => this.playTone(800, 80), 80);
	},

	startup() {
		this.playTone(400, 100);
		setTimeout(() => this.playTone(600, 150), 120);
		setTimeout(() => this.playTone(800, 100), 280);
	}
};

// --- Música de Fondo ---
function initBackgroundMusic() {
	const music = document.getElementById('background-music');
	if (music && SFX.enabled) {
		music.volume = 0.25;
		music.play().catch(() => {
			// Algunos navegadores requieren interacción del usuario
			console.log('Música de fondo requiere interacción del usuario');
		});
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
			card.title = `Tipo: ${pk.tipo1}${pk.tipo2 ? '/' + pk.tipo2 : ''}\nColor: ${pk.color}\nHabitat: ${pk.habitat}\nPeso: ${pk.peso || '-'}kg\nAltura: ${pk.altura || '-'}m\nGrupo huevo: ${pk.huevo || '-'}\nRareza: ${pk.rareza || '-'}\n${pk.legendario ? 'Legendario' : ''}`;
			
			// Agregar sonidos y animaciones al hover
			if (isCandidate) {
				card.addEventListener('mouseenter', () => {
					SFX.hover();
				});
				card.addEventListener('click', () => {
					SFX.select();
				});
			}
			
			grid.appendChild(card);
		});
}

// --- Elige la siguiente pregunta útil ---
function nextQuestion() {
	const q = pickBestQuestion();
	if (!q) { currentQuestion = null; return null; }
	currentQuestion = q;
	return q.text;
}

// --- Maneja la respuesta del usuario ---
function handleAnswer(isYes) {
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

// --- Decide si preguntar o adivinar ---
function askOrGuess() {
	const qText = nextQuestion();
	const qDiv = document.getElementById('question-text');
	const yesBtn = document.getElementById('yes-btn');
	const noBtn = document.getElementById('no-btn');
	if (candidates.length === 1) {
		qDiv.textContent = `¡Tu Pokémon es ${candidates[0].name.charAt(0).toUpperCase() + candidates[0].name.slice(1)}!`;
		yesBtn.disabled = true;
		noBtn.disabled = true;
		SFX.confirm();
	} else if (candidates.length === 0) {
		qDiv.textContent = "No hay coincidencias. ¿Seguro que tu Pokémon está en la lista?";
		yesBtn.disabled = true;
		noBtn.disabled = true;
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

// --- Reinicia el juego ---
function restartGame() {
	candidates = [...pokemonList];
	asked = [];
	currentQuestion = null;
	document.getElementById('question-text').textContent = "Piensa en un Pokémon y presiona 'SÍ' o 'NO' para comenzar.";
	document.getElementById('yes-btn').disabled = false;
	document.getElementById('no-btn').disabled = false;
	renderGrid();
}

// --- Eventos de botones ---
document.getElementById('yes-btn').onclick = () => { SFX.click(); handleAnswer(true); };
document.getElementById('no-btn').onclick = () => { SFX.click(); handleAnswer(false); };
document.getElementById('restart-btn').onclick = () => { SFX.startup(); restartGame(); };
const soundToggle = document.getElementById('sound-toggle');
if (soundToggle) {
	soundToggle.onclick = () => {
		SFX.enabled = !SFX.enabled;
		SFX.musicEnabled = SFX.enabled;
		
		const music = document.getElementById('background-music');
		if (music) {
			if (SFX.enabled) {
				music.volume = 0.25;
				music.play().catch(() => {});
				soundToggle.textContent = '🔊';
			} else {
				music.pause();
				soundToggle.textContent = '🔈';
			}
		}
	};
}

// --- Inicialización ---
window.onload = () => {
	candidates = [...pokemonList];
	asked = [];
	currentQuestion = null;
	renderGrid();
	document.getElementById('question-text').textContent = "Piensa en un Pokémon y presiona 'SÍ' o 'NO' para comenzar.";
	document.getElementById('yes-btn').disabled = false;
	document.getElementById('no-btn').disabled = false;
	// Rebuild questions in case pokemonList changed
	questions = buildQuestions();
	
	// Iniciar sonido de startup
	setTimeout(() => SFX.startup(), 300);
	
	// Intentar reproducir música de fondo con interacción del usuario
	document.addEventListener('click', () => {
		if (SFX.enabled && SFX.musicEnabled) {
			const music = document.getElementById('background-music');
			if (music && music.paused) {
				music.volume = 0.25;
				music.play().catch(() => {});
			}
		}
	}, { once: true });
};
// script.js - Plantilla base para videojuego web



