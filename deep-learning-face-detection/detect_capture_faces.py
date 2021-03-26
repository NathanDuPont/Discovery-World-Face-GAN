# python detect_capture_faces.py --video swing.mp4

from imutils.video import FileVideoStream
import numpy as np
import argparse
import imutils
import cv2
import os

# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", required=True,
#                 help="path to input video file")
# args = vars(ap.parse_args())

faces = []
video_file_name = 'swing.mp4'
confidence_threshold = 0.5
model = cv2.dnn.readNetFromCaffe('model/deploy.prototxt.txt', "model/opencv_face_detector.caffemodel")
file_name_no_ext = video_file_name.split('.')[0]
face_directory = f'{file_name_no_ext}-faces'
if not os.path.exists(face_directory):
    os.makedirs(face_directory)

video_stream = FileVideoStream(video_file_name).start()


while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = video_stream.read()

    if frame is None:
        break

    frame = imutils.resize(frame, width=400)

    # grab the frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the detections and
    # predictions
    model.setInput(blob)
    detections = model.forward()

    # we only care about detections which are greater than the threshold
    num_detections = detections.shape[2]
    detections = detections[0, 0, detections[0, 0, 0:num_detections, 2] > confidence_threshold, 0:7]

    if detections.size > 0:

        # get the size of each box as the sum of two sides of the rectangle
        num_detections = detections.shape[0]
        sizes = ((detections[0:num_detections, 5] - detections[0:num_detections, 3])
                 + (detections[0:num_detections, 6] - detections[0:num_detections, 4]))

        # print(detections[0:num_detections, 5])
        # print(detections[0:num_detections, 3])
        # print(detections[0:num_detections, 6])
        # print(detections[0:num_detections, 4])
        # print()

        # get the largest box
        ordered_sizes = -sizes.argsort()

        if sizes[ordered_sizes[0]] > .5:
            box = detections[ordered_sizes[0], 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            faces.append(frame[startY:endY, startX:endX])

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# write all the faces to a file
for i, face in enumerate(faces):
    cv2.imwrite(f'{face_directory}/face{i}.jpg', face)

# do a bit of cleanup
cv2.destroyAllWindows()
video_stream.stop()
