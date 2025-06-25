import win32api


def list_drives() -> list[str]:
    return win32api.GetLogicalDriveStrings().split('\000')[:-1]


def is_drive_pico(drive: str) -> bool:
    return win32api.GetVolumeInformation(drive)[0] == 'RPI-RP2'
