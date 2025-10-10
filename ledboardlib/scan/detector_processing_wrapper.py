import queue
from multiprocessing import Queue

from ledboardlib.scan.detector import Detector
from ledboardlib.scan.detector_options import DetectorOptions
from ledboardlib.scan.frame_detection_result import FrameDetectionResult


def run_detection_in_process(result_queue: "Queue[FrameDetectionResult]", command_queue: "Queue[str]", options: DetectorOptions):
    """
    Ensures communication with the parent process when executed in a separate process.
    """
    detector = Detector(options)
    detector.begin()

    while True:
        try:
            # FIXME find out why not working on exit (maybe KeyboardInterrupt is propagated down?)
            if not command_queue.empty():
                command = command_queue.get(block=False)
                print(f"Received command: {command}")
                if command == "stop":
                    break

            result = detector.step()
            try:
                result_queue.put(result, block=False)
            except queue.Full:
                pass

        except KeyboardInterrupt:
            break

    detector.end()
    print("Detection execution in process ended")
