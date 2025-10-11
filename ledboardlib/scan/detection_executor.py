import logging
import queue
from multiprocessing import Event, Process, Queue
from multiprocessing.synchronize import Event as EventType

from ledboardlib.scan.detector_options import DetectorOptions
from ledboardlib.scan.detector_processing_wrapper import run_detection_in_process
from ledboardlib.scan.frame_detection_result import FrameDetectionResult


_logger = logging.getLogger("DetectionExecutor")


class DetectionExecutor:
    """
    Executes DetectorProcessingWrapper in a separate process.
    """
    def __init__(self, options: DetectorOptions):
        self._options = options

        self._end_event: EventType | None = None
        self._options_queue: Queue | None = None
        self._result_queue: Queue | None = None
        self._process: Process | None = None
        self._is_running = False

    def get_options(self) -> DetectorOptions:
        return self._options

    def set_options(self, options: DetectorOptions):
        self._options = options

    def start(self) -> bool:
        if self._process or self._is_running:
            _logger.info("Detector process already running")
            return False

        _logger.info("Starting detector process...")
        self._end_event = Event()
        self._result_queue = Queue(maxsize=1)
        self._options_queue = Queue(maxsize=1)
        self._options_queue.put(self._options)
        self._process = Process(
            target=run_detection_in_process,
            args=(
                self._end_event,
                self._result_queue,
                self._options_queue,
            )
        )
        self._process.start()
        self._is_running = True

        return True

    def stop(self) -> bool:
        if not (self._process and self._is_running):
            _logger.info("Detector process not running")
            return False

        _logger.info("Stopping detector process...")
        if self._process.is_alive():
            self._end_event.set()
            self._process.join(timeout=5)
            if self._process.is_alive():
                _logger.info("/!\ Force terminating detector process...")
                self._process.terminate()

        _logger.info("Scanner process stopped")
        self._end_event = None
        self._options_queue = None
        self._result_queue = None

        self._process = None
        self._is_running = False

        return True

    def get_latest_result(self) -> FrameDetectionResult | None:
        """
        Get the latest scan result from the child process.

        Returns:
            FrameDetectionResult containing the brightest point and image data, or None if no data available
        """
        if self._process is None or not self._process.is_alive():
            raise RuntimeError("Detector process not running")

        try:
            self._options_queue.put(self._options, timeout=0.01)
        except queue.Full:
            pass

        try:
            return self._result_queue.get(timeout=0.01)
        except queue.Empty:
            pass

        return None

    @property
    def is_running(self) -> bool:
        return self._is_running
