import json
import math
import os
from enum import Enum

from ledboardlib import BoardApi, ColorFormat, GpioEnum, SamplingPoint, InteropDataStore


def main(port:str, update_board_config:bool, update_board_points: bool, save_to_json: bool, scanned_points_filepath: str):
    points = []
    with open(scanned_points_filepath, "r") as file:
        points = json.load(file)

    distances = compute_distances(points)
    average_distance = sum(distances) / len(distances)
    print(f"Average distance: {average_distance}, for {len(distances)} segments")

    filtered_distances = []
    for distance in distances:
        if distance <= average_distance * 3:
            filtered_distances.append(distance)

    average_filtered_distance = sum(filtered_distances) / len(filtered_distances)
    print(f"Average filtered distance: {average_filtered_distance}, for {len(filtered_distances)} segments")

    scaled_points = [(x / average_filtered_distance, y / average_filtered_distance) for x, y in points]
    scaled_distances = compute_distances(scaled_points)
    average_distance_scaled = sum(scaled_distances) / len(scaled_distances)

    strand_led_count = 600

    strand_count = 1
    pixel_doubling = 1
    sampling_points = list()
    for index, (x, y) in enumerate(scaled_points):
        new = SamplingPoint(
            index=index,
            x=int(x),
            y=int(y),
            universe_number=0,
            universe_channel=index * 3,
            color_format=ColorFormat.GRB,
            led_indices=[index]
        )
        sampling_points.append(new)

    print(f"Sampling points: {len(sampling_points)}")

    if save_to_json:
        with open("sampling-points-melinerion.json", "w+") as file:
            json.dump(
                [sampling_point.to_dict() for sampling_point in sampling_points],
                file,
                indent=2,
                default=lambda o: o.value if isinstance(o, Enum) else o.__dict__
            )

        interop_store = InteropDataStore(find_interop_file())
        interop_store.data.sampling_points = sampling_points
        interop_store.save()

    board = BoardApi(serial_port_name=port)
    if update_board_config:
        configuration = board.get_configuration()
        configuration.name = "Meliner"
        configuration.led_color_format = ColorFormat.GRBW
        configuration.led_count = strand_led_count
        configuration.gpio_led_first = GpioEnum.LedsNoonBoard.value
        configuration.gpio_dmx_input = GpioEnum.DmxNoonBoard.value
        configuration.gpio_dip_switch_first = GpioEnum.DipSwitchNoonBoard.value
        configuration.dmx_address = 80  # DIP switch pin 7 not working, keep setting value here
        board.set_configuration(configuration)

        print(configuration)

    if update_board_points:
        board.set_sampling_points(sampling_points)


def compute_distances(points_):
    distances_ = []
    for i in range(len(points_) - 1):
        x0, y0 = points_[i]
        x1, y1 = points_[i + 1]
        distances_.append(math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2))
    return distances_


def find_interop_file(root='.') -> str | None:
    root = os.path.abspath(root)

    for dir_ in os.listdir(root):
        candidate = os.path.join(root, dir_, "ledboardtranslatoremulator/resources/interop-data-melinerion.json")
        if os.path.exists(candidate):
            return candidate

    upper = os.path.dirname(root)
    if upper == root:
        return None

    return find_interop_file(upper)


if __name__ == "__main__":
    main(
        port="COM17",
        update_board_config=True,
        update_board_points=False,
        save_to_json=False,
        scanned_points_filepath="detec-melinerion-22-10-2025.json"
    )
