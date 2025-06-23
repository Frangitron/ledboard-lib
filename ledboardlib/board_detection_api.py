import serial.tools.list_ports

from ledboardlib.board_api import BoardApi
from ledboardlib.listed_board import ListedBoard


class BoardDetectionApi:

    def list_boards(self) -> list[ListedBoard]:
        port_names = [p.name for p in serial.tools.list_ports.comports()]
        listed_boards = list()
        for port_name in port_names:
            try:
                board = BoardApi(serial_port=port_name)
                board_info = board.get_hardware_info()
            except serial.serialutil.SerialException:
                board_info = None

            listed_boards.append(ListedBoard(
                serial_port_name=port_name,
                available=board_info is not None,
                hardware_info=board_info
            ))

        return listed_boards
