import tensorflow as tf

from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.applications import ResNet50
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense

from tensorflow.keras.models import load_model

from keras import backend as K

from os import path


class RetionpathyClassificationModel:
    def __init__(self, static_files_path):
        self.session = K.get_session()
        self.graph = tf.get_default_graph()
        self.RestNet50 = None
        self.root_path = static_files_path
        print("RetionpathyClassificationModel INIT!")

    def create_model(self):
        with self.graph.as_default():

            weights_path = path.join(
                self.root_path,
                'static',
                'best.hdf5')

            set_session(self.session)
            self.RestNet50 = load_model(weights_path)

    def predict_class(self, image):
        with self.graph.as_default():
            set_session(self.session)

            scaled_image = image/255.
            y_pred = self.RestNet50.predict_classes([[scaled_image]])
            confidence = self.RestNet50.predict([[scaled_image]])

            print("RESULTS:")
            print(confidence)
            print(y_pred)

            print("Class:")
            if y_pred[0][0] == 1:
                print("Yes")
                confidence_str = "{0:.3f}".format(confidence[0][0])
                return ("Yes", confidence_str)
            else:
                print("No")
                confidence_str = "{0:.3f}".format(1 - confidence[0][0])
                return ("No", confidence_str)
