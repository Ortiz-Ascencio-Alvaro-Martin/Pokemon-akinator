// script.js - Plantilla base para videojuego web

document.getElementById('start-btn').onclick = function() {
    document.getElementById('main-menu').style.display = 'none';
    document.getElementById('game-area').style.display = '';
    document.getElementById('game-over').style.display = 'none';
    // Aquí puedes inicializar tu lógica de juego
};

document.getElementById('restart-btn').onclick = function() {
    document.getElementById('main-menu').style.display = '';
    document.getElementById('game-area').style.display = 'none';
    document.getElementById('game-over').style.display = 'none';
};

// Puedes agregar aquí más lógica para tu videojuego
