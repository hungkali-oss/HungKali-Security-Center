from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)

from PySide6.QtCore import QTimer

import json
import os


class ThreatPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Threat Center")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#00ff99;
        """)

        layout.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Time",
            "Severity",
            "Source",
            "Destination",
            "Signature",
        ])

        layout.addWidget(self.table)

        self.setLayout(layout)

        self.timer = QTimer()

        self.timer.timeout.connect(self.load_events)

        self.timer.start(2000)

        self.load_events()

    def load_events(self):

        path = "/var/log/suricata/eve.json"

        if not os.path.exists(path):
            return

        rows = []

        with open(path, "r", errors="ignore") as f:

            for line in f.readlines()[-100:]:

                try:
                    event = json.loads(line)

                    if event.get("event_type") != "alert":
                        continue

                    alert = event["alert"]

                    rows.append([
                        event.get("timestamp", "")[:19],
                        str(alert.get("severity", "")),
                        event.get("src_ip", ""),
                        event.get("dest_ip", ""),
                        alert.get("signature", ""),
                    ])

                except Exception:
                    pass

        self.table.setRowCount(len(rows))

        for r, row in enumerate(rows):

            for c, value in enumerate(row):

                self.table.setItem(
                    r,
                    c,
                    QTableWidgetItem(value),
                )

        self.table.resizeColumnsToContents()