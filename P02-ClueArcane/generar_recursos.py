"""
╔══════════════════════════════════════════════════════════════════╗
║          GENERADOR DE RECURSOS: Sonidos e Imágenes              ║
║           Para CLUE ARCANE - Universo de Arcane                 ║
╚══════════════════════════════════════════════════════════════════╝

Script que genera automáticamente:
- Archivos de sonido .wav (música y efectos)
- Imágenes PNG (fondos, personajes, íconos)
"""

import numpy as np
import os
from scipy.io import wavfile
from PIL import Image, ImageDraw, ImageFont
import math


class GeneradorRecursos:
    """
    Genera automáticamente recursos multimedia para el juego.
    Incluye sonidos y imágenes temáticas de Arcane.
    """
    
    def __init__(self):
        """Inicializa el generador y crea carpetas si no existen"""
        self.carpeta_sonidos = "assets/sonidos"
        self.carpeta_imagenes = "assets/imagenes"
        
        # Crear carpetas si no existen
        os.makedirs(self.carpeta_sonidos, exist_ok=True)
        os.makedirs(self.carpeta_imagenes, exist_ok=True)
        
        # Parámetros de audio
        self.sample_rate = 44100  # Hz
        self.duracion_corta = 0.5  # segundos
        self.duracion_media = 1.0
        self.duracion_larga = 2.0
        
        # Colores temáticos Arcane (RGB)
        self.color_piltover = (30, 144, 200)      # Azul
        self.color_zaun = (255, 140, 0)           # Naranja
        self.color_fondo_oscuro = (20, 20, 30)    # Oscuro
        self.color_blanco = (255, 255, 255)       # Blanco
        self.color_oro = (255, 215, 0)            # Oro
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Generar tono de frecuencia
    # ───────────────────────────────────────────────────────────────
    
    def generar_tono(self, frecuencia: float, duracion: float) -> np.ndarray:
        """
        Genera un tono de onda sinusoidal.
        
        Args:
            frecuencia: Frecuencia en Hz
            duracion: Duración en segundos
            
        Returns:
            Array de audio
        """
        t = np.linspace(0, duracion, int(self.sample_rate * duracion))
        audio = np.sin(2 * np.pi * frecuencia * t)
        return audio.astype(np.float32)
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Aplicar fade in/out
    # ───────────────────────────────────────────────────────────────
    
    def aplicar_fade(self, audio: np.ndarray, fade_duracion: float = 0.1) -> np.ndarray:
        """
        Aplica fade in/out al audio.
        
        Args:
            audio: Array de audio
            fade_duracion: Duración del fade en segundos
            
        Returns:
            Audio con fade aplicado
        """
        fade_samples = int(self.sample_rate * fade_duracion)
        
        # Fade in
        fade_in = np.linspace(0, 1, fade_samples)
        # Fade out
        fade_out = np.linspace(1, 0, fade_samples)
        
        audio[:fade_samples] *= fade_in
        audio[-fade_samples:] *= fade_out
        
        return audio
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Guardar archivo .wav
    # ───────────────────────────────────────────────────────────────
    
    def guardar_wav(self, audio: np.ndarray, nombre: str, carpeta: str):
        """
        Guarda audio como archivo .wav.
        
        Args:
            audio: Array de audio
            nombre: Nombre del archivo
            carpeta: Carpeta destino
        """
        # Normalizar audio
        audio = np.clip(audio, -1, 1)
        audio = (audio * 32767).astype(np.int16)
        
        # Guardar archivo
        ruta = os.path.join(carpeta, nombre)
        wavfile.write(ruta, self.sample_rate, audio)
        print(f"✓ {nombre} creado")
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODOS: Generar Sonidos Específicos
    # ───────────────────────────────────────────────────────────────
    
    def generar_musica_fondo(self):
        """Genera música de fondo oscura/ambient con atmósfera misteriosa."""
        duracion = 28.0
        total_samples = int(self.sample_rate * duracion)
        audio = np.zeros(total_samples, dtype=np.float32)

        tempo = 78
        beat = 60.0 / tempo
        compas = beat * 4
        segmento_samples = int(self.sample_rate * compas)

        # Progresión oscura en registro bajo.
        acordes = [
            (110.00, 164.81, 220.00),  # Am grave
            (98.00, 146.83, 196.00),   # Dm/G
            (82.41, 123.47, 164.81),   # Em
            (87.31, 130.81, 174.61),   # F
        ]
        bajos = [41.20, 36.71, 43.65, 49.00]

        def onda_ambient(freq: float, t_local: np.ndarray) -> np.ndarray:
            return (
                np.sin(2 * np.pi * freq * t_local)
                + 0.22 * np.sin(2 * np.pi * freq * 2.0 * t_local + 0.35)
                + 0.10 * np.sin(2 * np.pi * freq * 3.0 * t_local + 1.00)
            )

        num_segmentos = max(1, total_samples // segmento_samples)

        # Capa 1: pad armónico largo.
        for i in range(num_segmentos + 1):
            acorde = acordes[i % len(acordes)]
            inicio = i * segmento_samples
            fin = min(total_samples, inicio + segmento_samples)
            if inicio >= total_samples:
                break

            t_local = np.linspace(0, (fin - inicio) / self.sample_rate, fin - inicio, endpoint=False)
            pad = sum(onda_ambient(freq, t_local) for freq in acorde) / 3.0

            ataque = np.minimum(1.0, t_local / 0.9)
            release = np.minimum(1.0, (t_local[::-1]) / 1.1)
            envolvente = ataque * release
            audio[inicio:fin] += 0.29 * pad * envolvente

            # Capa 2: arpegio por pulso.
            for b in range(4):
                p_inicio = inicio + int(b * beat * self.sample_rate)
                p_fin = min(fin, p_inicio + int(0.65 * beat * self.sample_rate))
                if p_inicio >= fin:
                    continue
                tp = np.linspace(0, (p_fin - p_inicio) / self.sample_rate, p_fin - p_inicio, endpoint=False)
                freq = acorde[(b + 1) % 3] * 1.5
                arp = np.sin(2 * np.pi * freq * tp) + 0.12 * np.sin(2 * np.pi * freq * 2.0 * tp)
                env_arp = np.exp(-tp * 4.8)
                audio[p_inicio:p_fin] += 0.05 * arp * env_arp

        # Capa 3: bajo por compás.
        num_compases = int(duracion / compas) + 1
        for c in range(num_compases):
            freq_bajo = bajos[c % len(bajos)]
            inicio = int(c * compas * self.sample_rate)
            fin = min(total_samples, inicio + int(0.85 * compas * self.sample_rate))
            if inicio >= total_samples:
                break
            tb = np.linspace(0, (fin - inicio) / self.sample_rate, fin - inicio, endpoint=False)
            bajo = (
                np.sin(2 * np.pi * freq_bajo * tb)
                + 0.45 * np.sin(2 * np.pi * freq_bajo * 0.5 * tb)
                + 0.12 * np.sin(2 * np.pi * freq_bajo * 2.0 * tb)
            )
            env_bajo = np.exp(-tb * 2.5)
            audio[inicio:fin] += 0.18 * bajo * env_bajo

        # Capa extra: drone subgrave continuo.
        t_global = np.linspace(0, duracion, total_samples, endpoint=False)
        drone = (
            0.65 * np.sin(2 * np.pi * 34.0 * t_global)
            + 0.35 * np.sin(2 * np.pi * 51.0 * t_global + 0.9)
        )
        drone_env = 0.75 + 0.25 * np.sin(2 * np.pi * 0.06 * t_global)
        audio += 0.10 * drone * drone_env

        # Capa 4: pulso percusivo muy sutil para tensión.
        rng = np.random.default_rng(42)
        total_beats = int(duracion / beat)
        for b in range(total_beats):
            inicio = int(b * beat * self.sample_rate)
            fin = min(total_samples, inicio + int(0.14 * self.sample_rate))
            if inicio >= total_samples:
                break
            tp = np.linspace(0, (fin - inicio) / self.sample_rate, fin - inicio, endpoint=False)
            ruido = rng.uniform(-1.0, 1.0, fin - inicio)
            pulso = ruido * np.exp(-tp * 24.0)
            if b % 4 == 0:
                audio[inicio:fin] += 0.018 * pulso

        # Movimiento lento global.
        lfo = 0.90 + 0.10 * np.sin(2 * np.pi * 0.08 * t_global)
        audio *= lfo

        # Normalización suave y fade largo.
        max_abs = np.max(np.abs(audio))
        if max_abs > 0:
            audio = 0.92 * (audio / max_abs)

        audio = self.aplicar_fade(audio, 2.2)
        self.guardar_wav(audio, "musica_fondo.wav", self.carpeta_sonidos)
    
    def generar_pista_buena(self):
        """Genera sonido de pista positiva (Do mayor ascendente)"""
        # Secuencia: Do, Mi, Sol (Do Mayor)
        audio_total = np.array([])
        
        for frecuencia in [262, 330, 392]:  # Do, Mi, Sol
            audio = self.generar_tono(frecuencia, 0.2)
            audio = self.aplicar_fade(audio, 0.05)
            audio_total = np.concatenate([audio_total, audio])
        
        self.guardar_wav(audio_total, "pista_buena.wav", self.carpeta_sonidos)
    
    def generar_error(self):
        """Genera sonido de error (descarte)"""
        # Dos beeps descendentes
        audio = self.generar_tono(800, 0.1) / 2
        audio = np.concatenate([audio, np.zeros(int(self.sample_rate * 0.1))])
        audio = np.concatenate([audio, self.generar_tono(600, 0.1) / 2])
        
        audio = self.aplicar_fade(audio)
        self.guardar_wav(audio, "error.wav", self.carpeta_sonidos)
    
    def generar_investigacion(self):
        """Genera sonido de investigación (sonido sci-fi)"""
        # Sonido de exploración: barrido de frecuencia
        duracion = self.duracion_media
        t = np.linspace(0, duracion, int(self.sample_rate * duracion))
        
        # Barrido de frecuencia: 200 Hz a 800 Hz
        frecuencia_inicio = 200
        frecuencia_fin = 800
        frecuencia = frecuencia_inicio + (frecuencia_fin - frecuencia_inicio) * t / duracion
        
        # Generar barrido con fase
        fase = 2 * np.pi * frecuencia_inicio * t + \
               2 * np.pi * (frecuencia_fin - frecuencia_inicio) * t * t / (2 * duracion)
        
        audio = np.sin(fase) * 0.6
        audio = self.aplicar_fade(audio, 0.2)
        self.guardar_wav(audio, "investigacion.wav", self.carpeta_sonidos)
    
    def generar_interrogatorio(self):
        """Genera sonido de interrogatorio (misterioso)"""
        # Sonido bajo y amenazante
        duracion = self.duracion_media
        t = np.linspace(0, duracion, int(self.sample_rate * duracion))
        
        # Nota baja con vibrato
        audio = np.sin(2 * np.pi * 55 * t)  # Mi muy bajo
        vibrato = 0.8 * np.sin(2 * np.pi * 3 * t)
        audio = audio * (0.7 + 0.3 * vibrato) * 0.5
        
        audio = self.aplicar_fade(audio, 0.3)
        self.guardar_wav(audio, "interrogatorio.wav", self.carpeta_sonidos)
    
    def generar_victoria(self):
        """Genera sonido de victoria (fanfarria)"""
        # Fanfarria: Do, Mi, Sol, Do (Do Mayor ascendente y resolución)
        audio_total = np.array([])
        
        frecuencias = [262, 330, 392, 523]  # Do, Mi, Sol, Do alto
        duraciones = [0.3, 0.3, 0.3, 0.6]    # El último es más largo
        
        for freq, dur in zip(frecuencias, duraciones):
            audio = self.generar_tono(freq, dur) * 0.7
            audio = self.aplicar_fade(audio, 0.1)
            audio_total = np.concatenate([audio_total, audio])
        
        self.guardar_wav(audio_total, "victoria.wav", self.carpeta_sonidos)
    
    def generar_derrota(self):
        """Genera sonido de derrota (descendente triste)"""
        # Secuencia descendente: Do, La, Fa, Re bajo
        audio_total = np.array([])
        
        frecuencias = [262, 220, 175, 110]  # Descendente
        
        for freq in frecuencias:
            audio = self.generar_tono(freq, 0.3)
            audio = self.aplicar_fade(audio, 0.1)
            audio_total = np.concatenate([audio_total, audio])
        
        self.guardar_wav(audio_total, "derrota.wav", self.carpeta_sonidos)
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Generar todas las imágenes
    # ───────────────────────────────────────────────────────────────
    
    def generar_fondos(self):
        """Genera imágenes de fondo temáticas"""
        
        # Fondo Piltover (Azul)
        img_piltover = Image.new('RGB', (1200, 800), self.color_fondo_oscuro)
        draw = ImageDraw.Draw(img_piltover)
        
        # Gradiente azul
        for y in range(800):
            r = int(20 + (30 - 20) * (y / 800))
            g = int(20 + (144 - 20) * (y / 800))
            b = int(30 + (200 - 30) * (y / 800))
            draw.line([(0, y), (1200, y)], fill=(r, g, b))
        
        # Añadir texto
        draw.text((100, 350), "PILTOVER", fill=self.color_oro, font=None)
        img_piltover.save(os.path.join(self.carpeta_imagenes, "fondo_piltover.png"))
        print("✓ fondo_piltover.png creado")
        
        # Fondo Zaun (Naranja)
        img_zaun = Image.new('RGB', (1200, 800), self.color_fondo_oscuro)
        draw = ImageDraw.Draw(img_zaun)
        
        # Gradiente naranja
        for y in range(800):
            r = int(20 + (255 - 20) * (y / 800))
            g = int(20 + (140 - 20) * (y / 800))
            b = int(30 + (0 - 30) * (y / 800))
            draw.line([(0, y), (1200, y)], fill=(r, g, b))
        
        draw.text((100, 350), "ZAUN", fill=self.color_oro, font=None)
        img_zaun.save(os.path.join(self.carpeta_imagenes, "fondo_zaun.png"))
        print("✓ fondo_zaun.png creado")
    
    def generar_personajes(self):
        """Genera representaciones visuales de personajes"""
        
        personajes = {
            "personaje_vi": (200, 100, 150),           # Rosa
            "personaje_jinx": (255, 100, 200),         # Magenta
            "personaje_jayce": (100, 180, 255),        # Azul claro
            "personaje_silco": (200, 100, 50),         # Marrón
            "personaje_mel": (200, 150, 100)           # Beige
        }
        
        for nombre, color in personajes.items():
            img = Image.new('RGB', (200, 300), self.color_fondo_oscuro)
            draw = ImageDraw.Draw(img)
            
            # Dibujar cabeza (círculo)
            draw.ellipse([(50, 30), (150, 130)], fill=color, outline=self.color_oro, width=3)
            
            # Dibujar cuerpo (rectángulo)
            draw.rectangle([(60, 130), (140, 250)], fill=color, outline=self.color_oro, width=3)
            
            # Dibujar base
            draw.rectangle([(30, 250), (170, 300)], fill=self.color_oro, outline=self.color_oro)
            
            img.save(os.path.join(self.carpeta_imagenes, f"{nombre}.png"))
            print(f"✓ {nombre}.png creado")
    
    def generar_iconos(self):
        """Genera íconos para las acciones del juego"""
        
        iconos = {
            "icono_investigacion": "🔍",
            "icono_interrogatorio": "🎤",
            "icono_pistas": "📋",
            "icono_veredicto": "⚖️"
        }
        
        for nombre, color in [
            ("icono_investigacion", (100, 200, 255)),
            ("icono_interrogatorio", (200, 100, 50)),
            ("icono_pistas", (100, 200, 100)),
            ("icono_veredicto", (255, 200, 0))
        ]:
            img = Image.new('RGB', (128, 128), self.color_fondo_oscuro)
            draw = ImageDraw.Draw(img)
            
            # Dibujar círculo
            draw.ellipse([(10, 10), (118, 118)], fill=color, outline=self.color_oro, width=3)
            
            # Dibujar símbolo interno (cuadrado)
            draw.rectangle([(40, 40), (88, 88)], fill=self.color_oro, outline=self.color_oro)
            
            img.save(os.path.join(self.carpeta_imagenes, f"{nombre}.png"))
            print(f"✓ {nombre}.png creado")
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Generar todos los recursos
    # ───────────────────────────────────────────────────────────────
    
    def generar_todos(self):
        """
        Genera todos los recursos (sonidos e imágenes).
        Este es el método principal a ejecutar.
        """
        print("\n" + "="*60)
        print("🎵 GENERANDO SONIDOS")
        print("="*60)
        
        self.generar_musica_fondo()
        self.generar_pista_buena()
        self.generar_error()
        self.generar_investigacion()
        self.generar_interrogatorio()
        self.generar_victoria()
        self.generar_derrota()
        
        print("\n" + "="*60)
        print("🖼️  GENERANDO IMÁGENES")
        print("="*60)
        
        self.generar_fondos()
        self.generar_personajes()
        self.generar_iconos()
        
        print("\n" + "="*60)
        print("✅ ¡TODOS LOS RECURSOS GENERADOS CORRECTAMENTE!")
        print("="*60)
        print("\n📁 Ubicaciones:")
        print(f"   • Sonidos: {self.carpeta_sonidos}/")
        print(f"   • Imágenes: {self.carpeta_imagenes}/")
        print("\n🎮 El juego GUI usará estos recursos automáticamente.")
        print("   Ejecuta: python ClueArcane_GUI.py\n")


# ═══════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL
# ═══════════════════════════════════════════════════════════════════

def main():
    """Punto de entrada: genera todos los recursos"""
    generador = GeneradorRecursos()
    generador.generar_todos()


if __name__ == "__main__":
    main()
