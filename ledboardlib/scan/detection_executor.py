from multiprocessing import Process, Queue

from ledboardlib.scan.detector_options import DetectorOptions
from ledboardlib.scan.detector_processing_wrapper import run_detection_in_process
from ledboardlib.scan.frame_detection_result import FrameDetectionResult


class DetectionExecutor:
    """
    Executes DetectorProcessingWrapper in a separate process.
    """
    def __init__(self, options: DetectorOptions, max_queue_size: int = 10):
        self.options = options

        self.result_queue = Queue(maxsize=max_queue_size)
        self.command_queue = Queue()

        self._process: Process | None = None
        self._is_running = False

    def start(self) -> bool:
        if self._process or self._is_running:
            print("Detector process already running")
            return False

        print("Starting detector process...")
        self._process = Process(
            target=run_detection_in_process,
            args=(self.result_queue, self.command_queue, self.options)
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
            self.command_queue.put("stop")
            self._process.join(timeout=1)
            if self._process.is_alive():
                print("Force terminating detector process...")
                self._process.terminate()

        print("Scanner process stopped")
        self._is_running = False

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

        if not self.result_queue.empty():
            try:
                return self.result_queue.get(block=False)
            except Exception:
                pass

        return None

    @property
    def is_running(self) -> bool:
        return self._is_running
