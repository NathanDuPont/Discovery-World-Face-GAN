import FaceDetector as fd
import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
import torch
import torchvision
import numpy as np

def cycle_gan_model():
    opt = TestOptions().parse()  # get test options
    # hard-code some parameters for test
    opt.num_threads = 0   # test code only supports num_threads = 0
    opt.batch_size = 1    # test code only supports batch_size = 1
    opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
    opt.no_flip = True    # no flip; comment this line if results on flipped images are needed.
    opt.display_id = -1   # no visdom display; the test code saves the results to a HTML file.
    model = create_model(opt)      # create a model given opt.model and other options
    model.setup(opt)               # regular setup: load and print networks; create schedulers
    if opt.eval:
        model.eval()            # regular setup: load and print networks; create schedulers
    
    return model


if __name__ == '__main__':

    cycle_gan = cycle_gan_model()
    face_detect = fd.FaceDetector('faceDetectionModel/deploy.prototxt.txt', 'faceDetectionModel/opencv_face_detector.caffemodel')
    
    face = face_detect.detect_face_from_image('me.jpg')
    original_size = face.shape

    data = {"A": None, "A_paths": None}
    face = np.array([face])
    face = face.transpose([0,3,1,2])
    data['A'] = torch.FloatTensor(face)

    cycle_gan.set_input(data)  # unpack data from data loader
    cycle_gan.test()

    result_image = cycle_gan.get_current_visuals()['fake']
    torchvision.utils.save_image(result_image, 'memonet.jpg')


    print('test')