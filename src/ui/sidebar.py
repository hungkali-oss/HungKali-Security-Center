from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
)


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)

        layout = QVBoxLayout()

        self.setLayout(layout)

        buttons = [
            "Dashboard",
            "Security",
            "Network",
            "Threat",
            "Logs",
            "Tools",
            "Settings",
        ]

        for name in buttons:

            btn = QPushButton(name)

            btn.setMinimumHeight(45)

            layout.addWidget(btn)

        layout.addStretch()