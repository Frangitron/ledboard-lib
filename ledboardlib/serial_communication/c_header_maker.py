import argparse
import logging
from typing import Any

import sys

from pythonarduinoserial.c_header_exporter import CHeaderExporter

from ledboardlib.serial_communication import all_structs


def make_c_header(structs: list[Any], filepath: str, display: bool):
    print("Generating C Header...")

    c_header_exporter = CHeaderExporter(
        struct_types=structs,
        namespace="Frangitron",
        include_guard_name="PLATFORMIO_SERIALPROTOCOL_H"
    )

    content = c_header_exporter.export()

    if display:
        print("")
        print("---------- FILE CONTENT ------------")
        print(content)
        print("-------- FILE CONTENT END ----------")
        print("")
    else:
        with open(filepath, "w+") as c_header_file:
            c_header_file.write(content)

    print(f"Destination {filepath}")
    print(f"Exported structs")
    print(" - " + "\n - ".join([struct.__name__ for struct in structs]))


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    parser = argparse.ArgumentParser(description="RP2040 LED Board - C Header exporter")
    parser.add_argument("--export-header", "-e", required=True, help="Export C Header to given filepath")
    parser.add_argument("--display-header", "-d", action="store_true", help="Print C Header to stdout")
    args, _ = parser.parse_known_args()

    make_c_header(
        structs=all_structs.get(),
        filepath=args.export_header,
        display=args.display_header
    )
