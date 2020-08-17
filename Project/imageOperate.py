import os

import numpy as np
import tensorflow as tf
from PIL import Image

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER + '/data', 'my_model.h5')
model = tf.keras.models.load_model(my_file)


def process(image):
    img = Image.open(image).convert('L')
    if img.size[0] != 28 or img.size[1] != 28:
        img = img.resize((28, 28))
    img = np.array(img).reshape((1, 28, 28))
    return img / 255.0


def predict(image):
    predictions = model.predict(image)
    label = np.argmax(predictions[0])
    return label
