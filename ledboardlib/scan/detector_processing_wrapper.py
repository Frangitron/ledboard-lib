import logging
import queue
from multiprocessing import Queue
from multiprocessing.synchronize import Event as EventType

from ledboardlib.scan.detector import Detector
from ledboardlib.scan.detector_options import DetectorOptions
from ledboardlib.scan.frame_detection_result import FrameDetectionResult


def run_detection_in_process(end_event: EventType, result_queue: "Queue[FrameDetectionResult]", options_queue: "Queue[DetectorOptions]"):
    """
    Ensures communication with the parent process when executed in a separate process.
    """
    logging.basicConfig(level=logging.INFO)

    options = options_queue.get(block=True)
    detector = Detector(options)
    detector.begin()

    while not end_event.is_set():
        try:
            options = options_queue.get(timeout=0.01)
            if options is not None:
                detector.set_options(options)
        except queue.Empty:
            pass

        try:
            result = detector.step()
            result_queue.put(result, timeout=0.01)
        except queue.Full:
            pass

    detector.end()

    while not options_queue.empty():
        options_queue.get()

    while not result_queue.empty():
        result_queue.get()
