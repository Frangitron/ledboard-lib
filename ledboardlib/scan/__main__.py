import cv2
import numpy as np
import time

from ledboardlib.scan.detection_executor import DetectionExecutor
from ledboardlib.scan.detector_options import DetectorOptions


detector = DetectionExecutor(options=DetectorOptions(
    camera_index=0,
    camera_width=640,
    camera_height=480,
    brightness_threshold=200,
))


def decode_image(image_encoded: bytes) -> np.ndarray:
    nparr = np.frombuffer(image_encoded, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


def main():
    detector.start()
    while detector.is_running:
        try:
            result = detector.get_latest_result()
            if result is not None:
                image = decode_image(result.frame_as_bytes)
                for x, y in result.points:
                    cv2.circle(image, (x, y), 5, (0, 255, 0), 2)

                cv2.imshow("Brightest Pixels Scanner", image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break

            else:
                time.sleep(0.1)

        except KeyboardInterrupt:
            break

    detector.stop()
    cv2.destroyAllWindows()


main()
