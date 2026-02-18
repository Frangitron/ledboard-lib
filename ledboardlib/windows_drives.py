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
            name = win32api.GetVolumeInformation(drive)[0]
            return  name in ['RPI-RP2', 'RP2350']
        except pywintypes.error as e:
            raise OSError(e)
