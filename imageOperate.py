import numpy as np
import tensorflow as tf
from PIL import Image

model = tf.keras.models.load_model('my_model.h5')


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
