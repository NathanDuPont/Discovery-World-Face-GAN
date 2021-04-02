import cv2
import time
from imutils.video import VideoStream
import imutils
import numpy as np

net = cv2.dnn.readNetFromCaffe('model/deploy.prototxt.txt', 'model/opencv_face_detector.caffemodel')

vs = VideoStream(0).start()
time.sleep(2.0)

images = []

while(True):
    # Capture frame-by-frame
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    num_detections = detections.shape[2]
    confidences = detections[0, 0, 0:num_detections, 2]
    detections = detections[0, 0, confidences > 0.5, 0:7]

    if detections.size > 0:
        num_detections = detections.shape[0]
        sizes = ((detections[0:num_detections, 5] - detections[0:num_detections, 3])
                 + (detections[0:num_detections, 6] - detections[0:num_detections, 4]))

        box = detections[np.argmax(sizes), 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
                      (0, 0, 255), 2)

        maxY = frame.shape[0]
        maxX = frame.shape[1]

        pad_size = 20
        images.append(frame[max(startY - pad_size, 0):min(endY + pad_size, maxY), max(startX - pad_size, 0):min(endX + pad_size, maxX)])

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
vs.stop()
cv2.destroyAllWindows()

for i, image in enumerate(images):
    cv2.imwrite(f'camera_test/{i}.jpg', image)


