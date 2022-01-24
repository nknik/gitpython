from os import path
def check_reboot():
    """checks reboot required or not"""
    return path.exists("/run/reboot-required")
print(("reboot required" if check_reboot() else "not required"))
print(dir())
