import queue

import time
from multiprocessing import Process, Queue

from ledboardlib.scan.detector_options import DetectorOptions
from ledboardlib.scan.detector_processing_wrapper import run_detection_in_process
from ledboardlib.scan.frame_detection_result import FrameDetectionResult


class DetectionExecutor:
    """
    Executes DetectorProcessingWrapper in a separate process.
    """
    def __init__(self, options: DetectorOptions):
        self._options = options

        self._command_queue: Queue = None # FIXME use Event?
        self._options_queue: Queue = None # FIXME use Event?
        self._result_queue: Queue = None

        self._process: Process | None = None
        self._is_running = False

    def get_options(self) -> DetectorOptions:
        return self._options

    def set_options(self, options: DetectorOptions):
        self._options = options
        if self._options_queue is not None and not self._options_queue.full():
            self._options_queue.put(options, block=False)

    def start(self) -> bool:
        if self._process or self._is_running:
            print("Detector process already running")
            return False

        print("Starting detector process...")
        self._command_queue = Queue(maxsize=1)
        self._result_queue = Queue(maxsize=1)
        self._options_queue = Queue(maxsize=1)
        self._process = Process(
            target=run_detection_in_process,
            args=(
                self._command_queue,
                self._result_queue,
                self._options_queue,
                self._options
            )
        )
        self._process.start()
        self._is_running = True

        return True

    def stop(self) -> bool:
        if not (self._process and self._is_running):
            print("Detector process not running")
            return False

        print("Stopping detector process...")
        if self._process.is_alive():
            self._command_queue.put("stop", block=False)
            self._process.join(timeout=0.5)
            if self._process.is_alive():
                print("/!\ Force terminating detector process...")
                self._process.terminate()

        print("Scanner process stopped")
        self._is_running = False
        self._process = None

        return True

    def get_latest_result(self) -> FrameDetectionResult | None:
        """
        Get the latest scan result from the child process.

        Returns:
            FrameDetectionResult containing the brightest point and image data, or None if no data available
        """
        # TODO sure this is the best way to handle this?
        if self._process is None or not self._process.is_alive():
            self._is_running = False
            if self._process is not None and not self._is_running:
                self._drain_queues()

        if not self._result_queue.empty():
            try:
                return self._result_queue.get(block=False)
            except Exception:
                pass

        return None

    @property
    def is_running(self) -> bool:
        return self._is_running

    def _drain_queues(self):
        """Drain all remaining items from queues to prevent process hanging."""
        self._drain_result_queue()
        self._drain_command_queue()

    def _drain_result_queue(self):
        while not self._result_queue.empty():
            try:
                self._result_queue.get_nowait()
            except Exception:
                break

    def _drain_command_queue(self):
        while not self._command_queue.empty():
            try:
                self._command_queue.get_nowait()
            except Exception:
                break
