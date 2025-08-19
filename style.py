from PySide6.QtWidgets import QApplication
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR)

# Tema escuro customizado sem dependência do qdarktheme
dark_theme_qss = f"""
QMainWindow {{
    background-color: #2b2b2b;
    color: #ffffff;
}}

QWidget {{
    background-color: #2b2b2b;
    color: #ffffff;
}}

QLineEdit {{
    background-color: #3c3c3c;
    border: 2px solid #555555;
    border-radius: 5px;
    color: #ffffff;
    padding: 5px;
}}

QLineEdit:focus {{
    border: 2px solid {PRIMARY_COLOR};
}}

QPushButton {{
    background-color: #4a4a4a;
    border: 1px solid #666666;
    border-radius: 5px;
    color: #ffffff;
    padding: 8px;
}}

QPushButton:hover {{
    background-color: #5a5a5a;
    border: 1px solid #777777;
}}

QPushButton:pressed {{
    background-color: #3a3a3a;
    border: 1px solid #555555;
}}

QPushButton[cssClass="specialButton"] {{
    color: #fff;
    background: {PRIMARY_COLOR};
    border: 1px solid {DARKER_PRIMARY_COLOR};
}}

QPushButton[cssClass="specialButton"]:hover {{
    color: #fff;
    background: {DARKER_PRIMARY_COLOR};
    border: 1px solid {DARKEST_PRIMARY_COLOR};
}}

QPushButton[cssClass="specialButton"]:pressed {{
    color: #fff;
    background: {DARKEST_PRIMARY_COLOR};
    border: 1px solid {DARKEST_PRIMARY_COLOR};
}}

QLabel {{
    background-color: transparent;
    color: #cccccc;
}}

QMessageBox {{
    background-color: #2b2b2b;
    color: #ffffff;
}}

QMessageBox QPushButton {{
    background-color: {PRIMARY_COLOR};
    border: 1px solid {DARKER_PRIMARY_COLOR};
    border-radius: 3px;
    padding: 6px 15px;
    min-width: 60px;
}}
"""


def setupTheme():
    """
    Configura o tema escuro customizado sem dependência do qdarktheme.
    Funciona com todas as versões do Python.
    """
    app = QApplication.instance()
    if app:
        app.setStyleSheet(dark_theme_qss)