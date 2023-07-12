import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("browser.py", base=base)
]

options = {
    "build_exe": {
        "packages": ["PyQt5", "PyQt5.QtWidgets", "PyQt5.QtCore", "PyQt5.QtWebEngineWidgets"],
        "includes": [],
        "include_files": []
    }
}

setup(
    name="clawSearch",
    version="1.0",
    description="Special Browser for You",
    options=options,
    executables=executables
)
