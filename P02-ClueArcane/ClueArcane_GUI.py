"""
Launcher estable para la GUI actual.

Mantiene compatibilidad con el comando historico:
    python ClueArcane_GUI.py

Internamente ejecuta la version visual vigente:
    ClueArcane_GUI_v4_Visual.py
"""

from pathlib import Path
import runpy


if __name__ == "__main__":
    script_actual = Path(__file__).with_name("ClueArcane_GUI_v4_Visual.py")
    runpy.run_path(str(script_actual), run_name="__main__")
