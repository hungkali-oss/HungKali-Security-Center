from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStatusBar,
    QStackedWidget,
)

from src.ui.sidebar import Sidebar
from src.ui.dashboard import Dashboard
from src.ui.threat import ThreatPage


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

        # Sidebar
        self.sidebar = Sidebar()
        self.sidebar.pageChanged.connect(self.change_page)

        # Pages
        self.dashboard = Dashboard()
        self.threat = ThreatPage()

        self.stack = QStackedWidget()

        self.stack.addWidget(self.dashboard)      # index 0

        # Security
        self.stack.addWidget(QWidget())           # index 1

        # Network
        self.stack.addWidget(QWidget())           # index 2

        # Threat
        self.stack.addWidget(self.threat)         # index 3

        # Logs
        self.stack.addWidget(QWidget())           # index 4

        # Tools
        self.stack.addWidget(QWidget())           # index 5

        # Settings
        self.stack.addWidget(QWidget())           # index 6

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("System Ready")

    def change_page(self, index):
        self.stack.setCurrentIndex(index)