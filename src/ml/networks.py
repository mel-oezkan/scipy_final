import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers.pooling import MaxPool2D

class SimpleConv:
    
    @staticmethod
    def create_model():
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, 2, padding="same", activation="relu"),
            tf.keras.layers.MaxPool2D(2, 2),
            tf.keras.layers.Conv2D(32, 2, padding="same", activation="relu"),
            tf.keras.layers.MaxPool2D(2, 2),
            tf.keras.layers.Conv2D(32, 2, padding="same", activation="relu"),
            tf.keras.layers.MaxPool2D(2, 2),
            tf.keras.layers.Conv2D(32, 2, padding="same", activation="relu"),
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(2, activation="softmax")    
        ])

        return model