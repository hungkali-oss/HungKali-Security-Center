import sys

from PySide6.QtWidgets import QApplication

from src.main_window import MainWindow
from src.theme.theme import load_theme


def main():

    app = QApplication(sys.argv)

    load_theme(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()