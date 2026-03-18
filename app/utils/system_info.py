import subprocess
import uuid
import platform


def run_powershell(cmd):
    try:
        result = subprocess.check_output(
            ["powershell", "-Command", cmd],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        return result if result else "unknown"
    except:
        return "unknown"


def get_cpu_id():
    return run_powershell("(Get-CimInstance Win32_Processor).ProcessorId")


def get_bios_serial():
    return run_powershell("(Get-CimInstance Win32_BIOS).SerialNumber")


def get_motherboard():
    return run_powershell("(Get-CimInstance Win32_BaseBoard).SerialNumber")


def get_disk_serial():
    return run_powershell("(Get-CimInstance Win32_DiskDrive)[0].SerialNumber")


def get_uuid():
    return run_powershell("(Get-CimInstance Win32_ComputerSystemProduct).UUID")


def get_mac():
    return str(uuid.getnode())


def get_system_info():
    return {
        "cpu_id": get_cpu_id(),
        "bios": get_bios_serial(),
        "board": get_motherboard(),
        "disk": get_disk_serial(),
        "uuid": get_uuid(),
        "mac": get_mac(),
        "os": platform.system(),
    }