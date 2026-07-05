import subprocess


class Fail2BanService:

    @staticmethod
    def is_running():
        try:
            result = subprocess.run(
                ["systemctl", "is-active", "fail2ban"],
                capture_output=True,
                text=True,
                timeout=3,
            )

            return result.stdout.strip() == "active"

        except Exception:
            return False