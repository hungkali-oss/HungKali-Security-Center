from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class InfoCard(QFrame):

    def __init__(self, title, value="0"):
        super().__init__()

        self.setObjectName("InfoCard")

        layout = QVBoxLayout(self)

        self.title = QLabel(title)
        self.title.setObjectName("CardTitle")
        self.title.setAlignment(Qt.AlignCenter)

        self.value = QLabel(value)
        self.value.setObjectName("CardValue")
        self.value.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.value)
        layout.addStretch()

    def setValue(self, value):
        self.value.setText(str(value))