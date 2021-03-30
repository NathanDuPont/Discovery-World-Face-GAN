import FaceDetector as fd


if __name__ == '__main__':
    faceDetector = fd.FaceDetector('model/deploy.prototxt.txt', 'model/opencv_face_detector.caffemodel')

    fd.export_image_to_file('face_test', faceDetector.detect_face_from_image('me.jpg'))
