import tensorflow as tf
from tensorflow import keras

class CustomNet:
    @staticmethod
    def build(height, width, depth, num_classes=None):

        inputShape = (height, width, depth)
        chanDim = -1

        if keras.backend.image_data_format() == 'channel_first':
            inputShape = (depth, height, width)
            chanDim = 1

        model = keras.models.Sequential([
            keras.layers.Conv2D(32, 3, padding='same', activation='relu', 
                                input_shape=inputShape, name="conv1_input"),
            keras.layers.BatchNormalization(axis=chanDim),
            keras.layers.MaxPooling2D((3, 3), (2, 2)),
            keras.layers.Dropout(rate=0.25),
            keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
            keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
            keras.layers.BatchNormalization(axis=chanDim),
            keras.layers.MaxPooling2D((3, 3), (2, 2)),
            keras.layers.Dropout(rate=0.25),
            keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
            keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
            keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
            keras.layers.BatchNormalization(axis=chanDim),
            keras.layers.MaxPooling2D((3, 3), (2, 2)),
            keras.layers.Dropout(rate=0.25),
            keras.layers.Flatten(),
            keras.layers.Dense(256, 'relu'),
            keras.layers.Dense(128, 'relu'),
            keras.layers.BatchNormalization(),
            keras.layers.Dropout(rate=0.5),
            keras.layers.Dense(num_classes, 'softmax'),
            ])
        
        return model

# model = CustomNet.build(28, 28, 1, num_classes=27)
            
# plot_model(model, to_file=split(realpath(__file__))[0] + "\CustomNet.png", show_shapes=True)

