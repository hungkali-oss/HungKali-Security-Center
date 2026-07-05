from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar,
)

from PySide6.QtCore import QTimer

from src.monitor.system_monitor import SystemMonitor

from src.services.suricata_service import SuricataService

from src.services.fail2ban_service import Fail2BanService


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("HungKali Security Center")

        title.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
            color:#00ff99;
        """)

        layout.addWidget(title)

        # CPU
        self.cpu_label = QLabel("CPU")
        self.cpu_bar = QProgressBar()
        self.cpu_bar.setRange(0, 100)

        # RAM
        self.ram_label = QLabel("RAM")
        self.ram_bar = QProgressBar()
        self.ram_bar.setRange(0, 100)

        # Disk
        self.disk_label = QLabel("Disk")
        self.disk_bar = QProgressBar()
        self.disk_bar.setRange(0, 100)

        # Status
        self.suricata = QLabel("🟢 Suricata : Running")
        self.fail2ban = QLabel("🟢 Fail2Ban : Waiting")

        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_bar)

        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_bar)

        layout.addWidget(self.disk_label)
        layout.addWidget(self.disk_bar)

        layout.addWidget(self.suricata)
        layout.addWidget(self.fail2ban)

        layout.addStretch()

        # Timer cập nhật mỗi giây
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

        self.update_stats()

    def update_stats(self):
        cpu = SystemMonitor.cpu()
        ram = SystemMonitor.ram()
        disk = SystemMonitor.disk()

        self.cpu_label.setText(f"CPU : {cpu:.1f}%")
        self.cpu_bar.setValue(int(cpu))

        self.ram_label.setText(f"RAM : {ram:.1f}%")
        self.ram_bar.setValue(int(ram))

        self.disk_label.setText(f"Disk : {disk:.1f}%")
        self.disk_bar.setValue(int(disk))

        # Kiểm tra Suricata
        if SuricataService.is_running():
            self.suricata.setText("🟢 Suricata : Running")
        else:
            self.suricata.setText("🔴 Suricata : Stopped")

        # Kiểm tra Fail2Ban
        if Fail2BanService.is_running():
            self.fail2ban.setText("🟢 Fail2Ban : Running")
        else:
            self.fail2ban.setText("🔴 Fail2Ban : Stopped")