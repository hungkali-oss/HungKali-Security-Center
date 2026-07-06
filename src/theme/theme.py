from pathlib import Path


def load_theme(app):

    qss = Path(__file__).parent / "dark.qss"

    if qss.exists():

        with open(qss, "r", encoding="utf-8") as f:

            app.setStyleSheet(f.read())