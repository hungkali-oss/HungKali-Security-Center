import psutil
import shutil


class SystemMonitor:
    @staticmethod
    def cpu():
        return psutil.cpu_percent(interval=None)

    @staticmethod
    def ram():
        return psutil.virtual_memory().percent

    @staticmethod
    def disk():
        usage = shutil.disk_usage("/")
        return round((usage.used / usage.total) * 100, 1)

    @staticmethod
    def upload():
        return psutil.net_io_counters().bytes_sent

    @staticmethod
    def download():
        return psutil.net_io_counters().bytes_recv

    @staticmethod
    def boot_time():
        return psutil.boot_time()