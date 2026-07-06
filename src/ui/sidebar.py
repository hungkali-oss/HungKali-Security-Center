from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
)


class Sidebar(QWidget):

    pageChanged = Signal(int)

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)

        layout = QVBoxLayout()
        self.setLayout(layout)

        pages = [
            "Dashboard",
            "Security",
            "Network",
            "Threat",
            "Logs",
            "Tools",
            "Settings",
        ]

        for index, name in enumerate(pages):

            btn = QPushButton(name)
            btn.setMinimumHeight(45)

            btn.clicked.connect(
                lambda checked=False, i=index: self.pageChanged.emit(i)
            )

            layout.addWidget(btn)

        layout.addStretch()