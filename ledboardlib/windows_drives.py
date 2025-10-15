import os
if os.name != "nt":

    def list_drives() -> list[str]:
        return []


    def is_drive_pico(drive: str) -> bool:
        return False

else:

    import pywintypes
    import win32api


    def list_drives() -> list[str]:
        return win32api.GetLogicalDriveStrings().split('\000')[:-1]


    def is_drive_pico(drive: str) -> bool:
        try:
            return win32api.GetVolumeInformation(drive)[0] == 'RPI-RP2'
        except pywintypes.error as e:
            raise OSError(e)
