import psutil
import platform

def get_system_info():
    info = {}

    info["OS"] = platform.system()
    info["OS Version"] = platform.version()
    info["Processor"] = platform.processor()

    info["CPU Usage (%)"] = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    info["RAM Total (GB)"] = round(memory.total / (1024**3), 2)
    info["RAM Used (GB)"] = round(memory.used / (1024**3), 2)

    disk = psutil.disk_usage('/')
    info["Disk Total (GB)"] = round(disk.total / (1024**3), 2)
    info["Disk Used (GB)"] = round(disk.used / (1024**3), 2)

    return info