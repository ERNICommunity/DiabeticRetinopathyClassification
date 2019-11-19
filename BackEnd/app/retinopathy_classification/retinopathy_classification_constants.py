# -*- coding: utf-8 -*-

# Fixed for our Hot Dog & Pizza classes
NUM_CLASSES = 2

# Fixed for Hot Dog & Pizza color images
CHANNELS = 3

IMAGE_RESIZE = 224
RESNET50_POOLING_AVERAGE = 'avg'
DENSE_LAYER_ACTIVATION = 'sigmoid'
OBJECTIVE_FUNCTION = 'binary_crossentropy'

# The name of the .h5 file containing the pretrained weights for the ResNet50
WEIGHTS_FILE = 'resnet50_weights_notop.h5'

SCALE = 300
