from flask import Blueprint, request, jsonify

from keras.preprocessing.image import load_img

import numpy as np

from .retinopathy_classification_model import RetionpathyClassificationModel
from .retinopathy_classification_service import save_file, process_image
from .retinopathy_classification_constants import SCALE


retinopathy_classification_module = Blueprint(
        'retinopathy_classification',
        __name__,
        url_prefix='/',
        static_folder='../static')

retinopathy_classification_model = RetionpathyClassificationModel(
        static_files_path=retinopathy_classification_module.root_path)
retinopathy_classification_model.create_model()
retinopathy_classification_model.RestNet50.summary()


@retinopathy_classification_module.route('/load-model', methods=['GET'])
def load_model():
    global retinopathy_classification_model

    if retinopathy_classification_model.RestNet50 is not None:
        return "Model was already loaded!"

    retinopathy_classification_model.create_model()

    return "Model was loaded successfully!"


@retinopathy_classification_module.route('/predict', methods=['POST'])
def predict():
    global retinopathy_classification_model

    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file found'

    user_file = request.files['file']

    file_path = save_file(user_file,
                          retinopathy_classification_module.root_path)

    image = np.asarray(load_img(file_path, target_size=(224, 224)))

    (class_name, confidence) = retinopathy_classification_model.predict_class(image)

    return jsonify(className=class_name, confidence=confidence)


@retinopathy_classification_module.route('/predict_processed', methods=['POST'])
def predict_with_processing():
    global retinopathy_classification_model

    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file found'

    user_file = request.files['file']

    file_path = save_file(user_file,
                          retinopathy_classification_module.root_path)

    process_image(file_path, SCALE)

    image = np.asarray(load_img(file_path, target_size=(224, 224)))

    (class_name, confidence) = retinopathy_classification_model.predict_class(image)

    return jsonify(className=class_name, confidence=confidence)
