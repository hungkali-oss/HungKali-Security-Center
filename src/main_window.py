from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStatusBar,
)

from src.ui.sidebar import Sidebar
from src.ui.dashboard import Dashboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("HungKali Security Center")
        self.resize(1400, 850)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        central.setLayout(layout)

        self.sidebar = Sidebar()

        self.dashboard = Dashboard()

        layout.addWidget(self.sidebar)

        layout.addWidget(self.dashboard)

        self.status = QStatusBar()

        self.setStatusBar(self.status)

        self.status.showMessage("System Ready")