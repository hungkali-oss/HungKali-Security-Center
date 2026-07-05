import json


class EveReader:

    def __init__(self, path="/var/log/suricata/eve.json"):
        self.path = path
        self.position = 0

    def read_new_events(self):
        events = []

        with open(self.path, "r") as f:
            f.seek(self.position)

            for line in f:
                try:
                    events.append(json.loads(line))
                except Exception:
                    pass

            self.position = f.tell()

        return events