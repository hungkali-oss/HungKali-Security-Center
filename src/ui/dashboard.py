from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
)

from PySide6.QtCore import Qt, QTimer

from src.widgets.info_card import InfoCard

from src.monitor.system_monitor import SystemMonitor
from src.services.suricata_service import SuricataService
from src.services.fail2ban_service import Fail2BanService


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        # ===== Title =====
        title = QLabel("HungKali Security Center")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#00ff99;
        """)

        main_layout.addWidget(title)

        # ===== Cards =====
        grid = QGridLayout()

        self.cpu_card = InfoCard("CPU")
        self.ram_card = InfoCard("RAM")
        self.disk_card = InfoCard("DISK")

        self.threat_card = InfoCard("Threat Today", "0")
        self.critical_card = InfoCard("Critical", "0")
        self.service_card = InfoCard("Services", "0")

        grid.addWidget(self.cpu_card, 0, 0)
        grid.addWidget(self.ram_card, 0, 1)
        grid.addWidget(self.disk_card, 0, 2)

        grid.addWidget(self.threat_card, 1, 0)
        grid.addWidget(self.critical_card, 1, 1)
        grid.addWidget(self.service_card, 1, 2)

        main_layout.addLayout(grid)

        # ===== Services =====
        self.suricata = QLabel()
        self.fail2ban = QLabel()

        self.suricata.setStyleSheet("font-size:16px;")
        self.fail2ban.setStyleSheet("font-size:16px;")

        main_layout.addSpacing(15)
        main_layout.addWidget(self.suricata)
        main_layout.addWidget(self.fail2ban)

        main_layout.addStretch()

        # ===== Timer =====
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

        self.update_stats()

    def update_stats(self):

        cpu = SystemMonitor.cpu()
        ram = SystemMonitor.ram()
        disk = SystemMonitor.disk()

        self.cpu_card.setValue(f"{cpu:.1f}%")
        self.ram_card.setValue(f"{ram:.1f}%")
        self.disk_card.setValue(f"{disk:.1f}%")

        running = 0

        if SuricataService.is_running():
            self.suricata.setText("🟢 Suricata : Running")
            running += 1
        else:
            self.suricata.setText("🔴 Suricata : Stopped")

        if Fail2BanService.is_running():
            self.fail2ban.setText("🟢 Fail2Ban : Running")
            running += 1
        else:
            self.fail2ban.setText("🔴 Fail2Ban : Stopped")

        self.service_card.setValue(f"{running}/2")

        # Tạm thời để 0, sau sẽ đọc từ eve.json
        self.threat_card.setValue("0")
        self.critical_card.setValue("0")