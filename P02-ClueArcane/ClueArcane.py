"""
╔══════════════════════════════════════════════════════════════════╗
║         CLUE ARCANE: El Misterio de Piltover y Zaun              ║
║                   Simulador del Juego de Mesa                    ║
╚══════════════════════════════════════════════════════════════════╝

Simulador del juego "Clue" ambientado en el universo de Arcane.
El jugador debe descubrir quién cometió el crimen, dónde ocurrió
y qué arma se utilizó, a través de investigación e interrogatorios.
"""

import random
from typing import List, Dict, Tuple


# ═══════════════════════════════════════════════════════════════════
# CLASE PRINCIPAL: ClueArcane
# ═══════════════════════════════════════════════════════════════════

class ClueArcane:
    """
    Clase que gestiona toda la lógica del juego Clue Arcane.
    Incluye configuración de elementos, generación de soluciones,
    investigación y narrativa de finales.
    """
    
    # ───────────────────────────────────────────────────────────────
    # DEFINICIÓN DE ELEMENTOS DEL JUEGO (Temática Arcane)
    # ───────────────────────────────────────────────────────────────
    
    PERSONAJES = {
        "Vi": "Vigilante de la resistencia de Zaun",
        "Jinx": "Inventora de caos y destrucción",
        "Jayce": "Consejero Hextech de Piltover",
        "Silco": "Industrial del comercio en la Subraun",
        "Mel Medarda": "Diplomática de Noxus"
    }
    
    LOCACIONES = {
        "Laboratorio Hextech": "Centro de investigación mágica en Piltover",
        "The Last Drop": "Bar de la Subraun donde se reúnen conspiradores",
        "Consejo de Piltover": "Sede del poder político de la ciudad",
        "Puente del Progreso": "Frontera entre Piltover y Zaun",
        "Prisión de Stillwater": "Fortaleza de máxima seguridad"
    }
    
    ARMAS = {
        "Guanteletes Atlas": "Arma de combate cuerpo a cuerpo hextech",
        "Lanzacohetes Espinas": "Dispositivo explosivo caótico",
        "Jeringa de Shimmer": "Veneno que altera la realidad",
        "Núcleo Hextech": "Cristal de energía arcana destructiva",
        "Bomba de Fuego": "Explosivo incendiario casero"
    }
    
    def __init__(self):
        """
        Constructor: inicializa el juego, genera la solución aleatoria
        y prepara las variables de estado del jugador.
        """
        # Generar solución aleatoria (culpable, locación, arma)
        self.culpable = random.choice(list(self.PERSONAJES.keys()))
        self.locacion = random.choice(list(self.LOCACIONES.keys()))
        self.arma = random.choice(list(self.ARMAS.keys()))
        
        # Registros de lo que el jugador ha investigado
        self.pistas_descubiertas: List[str] = []
        self.personajes_descartados: List[str] = []
        self.locaciones_descartadas: List[str] = []
        self.armas_descartadas: List[str] = []
        
        # Control de juego
        self.ronda = 0
        self.juego_activo = True
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Mostrar menú principal
    # ───────────────────────────────────────────────────────────────
    
    def mostrar_menu_principal(self) -> int:
        """
        Muestra el menú principal del juego y captura la opción
        del jugador.
        
        Retorna:
            int: Opción seleccionada por el jugador (1-5)
        """
        print("\n" + "="*60)
        print("             🎭 CLUE ARCANE: El Misterio de Piltover 🎭")
        print("="*60)
        print("\n[1] Investigar una locación")
        print("[2] Interrogar a un personaje")
        print("[3] Ver pistas descubiertas")
        print("[4] Emitir veredicto (acusar)")
        print("[5] Salir del juego")
        print("\n" + "-"*60)
        
        while True:
            try:
                opcion = int(input("Selecciona una opción (1-5): "))
                if 1 <= opcion <= 5:
                    return opcion
                print("❌ Opción inválida. Intenta de nuevo.")
            except ValueError:
                print("❌ Debes ingresar un número.")
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Investigar una locación
    # ───────────────────────────────────────────────────────────────
    
    def investigar_locacion(self):
        """
        Permite al jugador investigar una locación y obtiene pistas
        basadas en la solución del crimen.
        """
        print("\n📍 INVESTIGACIÓN DE LOCACIONES")
        print("-"*60)
        
        # Mostrar opciones de locaciones disponibles
        locaciones_lista = list(self.LOCACIONES.keys())
        for i, loc in enumerate(locaciones_lista, 1):
            estado = "✓ Investigada" if loc in self.locaciones_descartadas else "○"
            print(f"[{i}] {loc:<30} {estado}")
        
        try:
            opcion = int(input("\nSelecciona una locación (número): ")) - 1
            if 0 <= opcion < len(locaciones_lista):
                locacion_seleccionada = locaciones_lista[opcion]
                self._processar_investigacion_locacion(locacion_seleccionada)
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Debes ingresar un número.")
    
    def _processar_investigacion_locacion(self, locacion: str):
        """
        Procesa la investigación de una locación específica.
        Si es la locación correcta, da una pista relevante.
        Si no, descarta esa locación.
        
        Args:
            locacion (str): Nombre de la locación a investigar
        """
        if locacion in self.locaciones_descartadas:
            print(f"\n⚠️  Ya investigaste {locacion}. No hay nada nuevo.")
            return
        
        self.locaciones_descartadas.append(locacion)
        
        if locacion == self.locacion:
            # PISTA POSITIVA: Se encontró evidencia en esta locación
            pista = f"🔍 Encontraste evidencia en {locacion}! El crimen ocurrió aquí."
            print(f"\n✨ {pista}")
            self.pistas_descubiertas.append(pista)
        else:
            # Descarta esta locación
            print(f"\n❌ Buscaste en {locacion} pero no encontraste nada relevante.")
            print(f"   → {locacion} queda descartada como escena del crimen.")
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Interrogar a un personaje
    # ───────────────────────────────────────────────────────────────
    
    def interrogar_personaje(self):
        """
        Permite al jugador interrogar a un personaje para obtener
        pistas sobre el culpable.
        """
        print("\n🎤 INTERROGATORIO DE PERSONAJES")
        print("-"*60)
        
        personajes_lista = list(self.PERSONAJES.keys())
        for i, per in enumerate(personajes_lista, 1):
            estado = "✓ Interrogado" if per in self.personajes_descartados else "○"
            print(f"[{i}] {per:<20} ({self.PERSONAJES[per]:<40}) {estado}")
        
        try:
            opcion = int(input("\nSelecciona un personaje (número): ")) - 1
            if 0 <= opcion < len(personajes_lista):
                personaje_seleccionado = personajes_lista[opcion]
                self._processar_interrogatorio(personaje_seleccionado)
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Debes ingresar un número.")
    
    def _processar_interrogatorio(self, personaje: str):
        """
        Procesa el interrogatorio de un personaje específico.
        Si es el culpable, da una pista incriminatoria.
        Si no, lo descarta como sospechoso.
        
        Args:
            personaje (str): Nombre del personaje a interrogar
        """
        if personaje in self.personajes_descartados:
            print(f"\n⚠️  Ya interrogaste a {personaje}. Sus coartadas son sólidas.")
            return
        
        self.personajes_descartados.append(personaje)
        
        if personaje == self.culpable:
            # PISTA POSITIVA: Comportamiento sospechoso
            pista = f"🚨 {personaje} muestra signos de culpabilidad. ¡Comportamiento sospechoso detectado!"
            print(f"\n✨ {pista}")
            self.pistas_descubiertas.append(pista)
        else:
            # Descarta este personaje
            print(f"\n{personaje} tiene una coartada sólida.")
            print(f"   → {personaje} queda descartado como sospechoso.")
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Ver pistas descubiertas
    # ───────────────────────────────────────────────────────────────
    
    def ver_pistas(self):
        """
        Muestra todas las pistas que el jugador ha descubierto hasta ahora.
        """
        print("\n📋 PISTAS DESCUBIERTAS")
        print("="*60)
        
        if not self.pistas_descubiertas:
            print("Aún no has descubierto pistas relevantes. Sigue investigando...")
        else:
            for i, pista in enumerate(self.pistas_descubiertas, 1):
                print(f"{i}. {pista}")
        
        print("\n" + "-"*60)
        print(f"Personajes descartados: {len(self.personajes_descartados)}/5")
        print(f"Locaciones descartadas: {len(self.locaciones_descartadas)}/5")
        print(f"Armas descartadas: {len(self.armas_descartadas)}/5")
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Emitir veredicto (acusar)
    # ───────────────────────────────────────────────────────────────
    
    def emitir_veredicto(self) -> bool:
        """
        Permite al jugador hacer su acusación final basada en su investigación.
        Compara la acusación con la solución real del caso.
        
        Retorna:
            bool: True si la acusación fue correcta, False si fue incorrecta
        """
        print("\n⚖️  TRIBUNAL FINAL - EMITIR VEREDICTO")
        print("="*60)
        print("\nDebes acusar a UN culpable, UNA locación y UN arma.")
        print("Si fallas, el juego termina.\n")
        
        # Seleccionar culpable
        personajes_lista = list(self.PERSONAJES.keys())
        print("\n🎭 CULPABLES SOSPECHOSOS:")
        for i, per in enumerate(personajes_lista, 1):
            print(f"[{i}] {per}")
        
        try:
            opcion = int(input("¿Quién es el culpable? (número): ")) - 1
            if not (0 <= opcion < len(personajes_lista)):
                print("❌ Opción inválida.")
                return False
            culpable_acusado = personajes_lista[opcion]
        except ValueError:
            print("❌ Debes ingresar un número.")
            return False
        
        # Seleccionar locación
        locaciones_lista = list(self.LOCACIONES.keys())
        print("\n📍 LOCACIONES SOSPECHOSAS:")
        for i, loc in enumerate(locaciones_lista, 1):
            print(f"[{i}] {loc}")
        
        try:
            opcion = int(input("¿Dónde ocurrió el crimen? (número): ")) - 1
            if not (0 <= opcion < len(locaciones_lista)):
                print("❌ Opción inválida.")
                return False
            locacion_acusada = locaciones_lista[opcion]
        except ValueError:
            print("❌ Debes ingresar un número.")
            return False
        
        # Seleccionar arma
        armas_lista = list(self.ARMAS.keys())
        print("\n🔫 ARMAS SOSPECHOSAS:")
        for i, arm in enumerate(armas_lista, 1):
            print(f"[{i}] {arm}")
        
        try:
            opcion = int(input("¿Qué arma se utilizó? (número): ")) - 1
            if not (0 <= opcion < len(armas_lista)):
                print("❌ Opción inválida.")
                return False
            arma_acusada = armas_lista[opcion]
        except ValueError:
            print("❌ Debes ingresar un número.")
            return False
        
        # Verificar si la acusación es correcta
        acusacion_correcta = (
            culpable_acusado == self.culpable and
            locacion_acusada == self.locacion and
            arma_acusada == self.arma
        )
        
        if acusacion_correcta:
            self._mostrar_final_ganador(culpable_acusado, locacion_acusada, arma_acusada)
            return True
        else:
            self._mostrar_final_perdedor(culpable_acusado, locacion_acusada, arma_acusada)
            return False
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Mostrar final ganador (5 finales distintos según culpable)
    # ───────────────────────────────────────────────────────────────
    
    def _mostrar_final_ganador(self, culpable: str, locacion: str, arma: str):
        """
        Muestra el final narrativo ganador basado en quién sea el culpable.
        Cada personaje tiene su propia historia única fiel al estilo Arcane.
        
        Args:
            culpable (str): El culpable correcto
            locacion (str): La locación correcta
            arma (str): El arma correcta
        """
        print("\n" + "🎬 "*20)
        print("\n✨ ¡ACUSACIÓN CORRECTA! ✨\n")
        
        # Historias narrativas distintas para cada culpable
        finales = {
            "Vi": self._final_vi,
            "Jinx": self._final_jinx,
            "Jayce": self._final_jayce,
            "Silco": self._final_silco,
            "Mel Medarda": self._final_mel
        }
        
        # Ejecutar el final correspondiente
        if culpable in finales:
            finales[culpable](locacion, arma)
    
    def _final_vi(self, locacion: str, arma: str):
        """FINAL 1: Vi - La vigilante justiciera"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║                    FINAL: VI - LA JUSTICIA                     ║
║                    "Proteger a Zaun"                           ║
╚════════════════════════════════════════════════════════════════╝

La investigación ha revelado la verdad: Vi actuó por necesidad, no por 
maldad. En {}, ella eliminó la amenaza utilizando {}.

"Alguien tenía que tomar medidas", explica con determinación. "El sistema 
de Piltover no iba a hacer nada. Lo hice para proteger mi gente."

El tribunal queda en silencio. Las pruebas son irrefutables, pero la 
motivación es comprensible. Vi es sentenciada a trabajar bajo vigilancia 
en la Subraun, asegurando que no haya futuras víctimas.

VEREDICTO: Culpable, pero justiciera. El futuro de Zaun descansa en sus 
manos redimidas.
        """.format(locacion, arma))
    
    def _final_jinx(self, locacion: str, arma: str):
        """FINAL 2: Jinx - El caos encarnado"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║              FINAL: JINX - EL CAOS ENCARNADO                   ║
║                    "Boom"                                      ║
╚════════════════════════════════════════════════════════════════╝

La prueba definitiva: Jinx fue quien actuó en {} con {}.

Pero lo más inquietante es su risa mientras se le presentan las pruebas.
"¿Caos?" pregunta con una sonrisa psicótica. "Eso fue un experimento."

No muestra arrepentimiento. Solo curiosidad por el resultado. En su mente 
fracturada, el crimen fue simplemente otra explosion hermosa en la sinfonia 
del caos.

Se la llevan en cadenas de Hextech, pero todos saben que ella ya está 
planeando su próximo "experimento" desde su celda.

VEREDICTO: Culpable. Peligrosa para la sociedad. Peligrosa para ella misma.
Tal vez especialmente peligrosa porque no le importa lo más mínimo.
        """.format(locacion, arma))
    
    def _final_jayce(self, locacion: str, arma: str):
        """FINAL 3: Jayce - El político ambicioso"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║           FINAL: JAYCE - LA AMBICIÓN SIN LÍMITES               ║
║                  "El Progreso a Cualquier Costo"               ║
╚════════════════════════════════════════════════════════════════╝

El Consejero Hextech Jayce fue quien actuó en {} con {}.

Su motivación: eliminar un obstáculo político. Su método: frío y calculado.
Jayce creía que era intocable, que su posición lo protegería.

Se equivocaba.

Las pruebas pintan un retrato de un hombre corrompido por el poder, 
dispuesto a cometer actos atroces para mantener su posición privilegiada.
"El progreso exige sacrificios," fue su único comentario.

Se lo llevan entre gritos de los ciudadanos de Zaun que exigen justicia.
Piltover ha caído. Su símbolo de brillo fue manchado de sangre.

VEREDICTO: Culpable. Condenado a prisión de por vida. Su nombre será 
recordado como el de un traidor.
        """.format(locacion, arma))
    
    def _final_silco(self, locacion: str, arma: str):
        """FINAL 4: Silco - El industrial de la Subraun"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║         FINAL: SILCO - EL PADRINO DE LA SUBRAUN                ║
║                   "Negocios de la Calle"                       ║
╚════════════════════════════════════════════════════════════════╝

La prueba apunta a Silco, el Industrial de la Subraun, quien actuó en 
{} utilizando {}.

El crimen fue un "ajuste de cuentas". Una venganza por negocios sin cerrar.
Silco permanece impasible, sus cicatrices rosados como un monumento a 
su despiadada eficiencia.

"Hice lo que debía hacerse," dice con voz tranquila. "En la Subraun, 
así es como funciona."

El tribunal reconoce que Silco es un síntoma de un problema mayor: un 
sistema que permite que tales figuras de las sombras gobiernen sin control.

VEREDICTO: Culpable. Pero el sistema que lo creó también lo es. Silco 
sonríe desde su celda. Sabe que su imperio continuará sin él.
        """.format(locacion, arma))
    
    def _final_mel(self, locacion: str, arma: str):
        """FINAL 5: Mel Medarda - La diplomática estratégica"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║         FINAL: MEL MEDARDA - LA DIPLOMACIA OSCURA              ║
║                   "Noxus Siempre Gana"                         ║
╚════════════════════════════════════════════════════════════════╝

Los documentos son incontrovertibles: Mel Medarda actuó en {} con {}.

Pero esto no era crimen pasional. Era estrategia política de Noxus.
Mel fue un agente toda la vida, posicionada para debilitar a Piltover
desde adentro.

"Piltover fue débil," explica sin emoción. "Noxus solo aceleró lo inevitable."

Su confesión implica a otras figuras prominentes. Piltover descubre que su 
círculo íntimo estaba infiltrado. El pánico se apodera de la ciudad.

Se la extraditará a Noxus para juicio, pero todos saben que nunca llegará.
Desaparecerá en las sombras de la política internacional.

VEREDICTO: Culpable de muchos crímenes. Pero el más grande crimen fue la 
confianza misma que Piltover le brindó.
        """.format(locacion, arma))
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Mostrar final perdedor
    # ───────────────────────────────────────────────────────────────
    
    def _mostrar_final_perdedor(self, culpable: str, locacion: str, arma: str):
        """
        Muestra el final cuando el jugador falla su acusación.
        
        Args:
            culpable (str): Lo que el jugador acusó (incorrecto)
            locacion (str): Lo que el jugador acusó (incorrecto)
            arma (str): Lo que el jugador acusó (incorrecto)
        """
        print("\n" + "❌ "*20)
        print("\n¡ACUSACIÓN INCORRECTA! \n")
        print("""
╔════════════════════════════════════════════════════════════════╗
║                    JUICIO FALLIDO                              ║
╚════════════════════════════════════════════════════════════════╝

Acusaste a {} de actuar en {} utilizando {}.

PERO... Tus pruebas son insuficientes. El tribunal revela la verdad:

""".format(culpable, locacion, arma))
        
        print(f"El verdadero culpable: {self.culpable}")
        print(f"Locación real: {self.locacion}")
        print(f"Arma utilizada: {self.arma}")
        
        print("""
El criminal escapó. Tu fracaso permitió que la injusticia prevaleciera.

En Piltover y Zaun, el caso permanecerá sin resolver. La verdadera 
víctima y los sospechosos incorrectamente acusados serán recordados en 
las sombras de este misterio.

VEREDICTO: JUICIO ANULADO. El crimen continúa impune.
        """)
    
    # ───────────────────────────────────────────────────────────────
    # MÉTODO: Ejecutar bucle principal del juego
    # ───────────────────────────────────────────────────────────────
    
    def ejecutar_juego(self):
        """
        Bucle principal que mantiene el juego activo hasta que:
        1. El jugador emite un veredicto (gana o pierde)
        2. El jugador decide salir
        """
        print("\n" + "="*60)
        print("    Bienvenido a CLUE ARCANE: El Misterio de Piltover")
        print("="*60)
        print("\nUn crimen ha sido cometido en Piltover y Zaun.")
        print("Tu misión: Investigar y descubrir al culpable.\n")
        
        while self.juego_activo:
            opcion = self.mostrar_menu_principal()
            
            if opcion == 1:
                # Investigar locación
                self.investigar_locacion()
            
            elif opcion == 2:
                # Interrogar personaje
                self.interrogar_personaje()
            
            elif opcion == 3:
                # Ver pistas descubiertas
                self.ver_pistas()
            
            elif opcion == 4:
                # Emitir veredicto
                resultado = self.emitir_veredicto()
                if resultado:
                    print("\n🎉 ¡GANASTE! Resolviste el misterio correctamente.")
                else:
                    print("\n😢 ¡PERDISTE! El culpable escapó.")
                
                self.juego_activo = False
            
            elif opcion == 5:
                # Salir del juego
                print("\nGracias por jugar CLUE ARCANE.")
                print("Que las sombras de Piltover y Zaun siempre guarden sus secretos...")
                self.juego_activo = False


# ═══════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL: Punto de entrada del programa
# ═══════════════════════════════════════════════════════════════════

def main():
    """
    Función principal que instancia el juego y lo ejecuta.
    FLUJO GENERAL:
    1. Crear instancia de ClueArcane
    2. Ejecutar bucle principal del juego
    3. El jugador investiga hasta descubrir el culpable
    """
    juego = ClueArcane()
    juego.ejecutar_juego()


if __name__ == "__main__":
    main()
