from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense, MaxPooling2D, Dropout
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator

NUM_CLASSES = 10


def train_and_eval_CNN(X_train, y_train, X_val, y_val, X_test, y_test):
    model = Sequential()
    model.add(
        Conv2D(32, (3, 3), padding="same", activation="relu", input_shape=(48, 48, 1))
    )
    model.add(Flatten())
    model.add(Dense(10, activation="softmax"))
    # model.add(MaxPooling2D(pool_size=(2, 2)))

    # model.add(Dense(128, activation="relu"))
    # model.add(Dropout(0.5))

    # Compile the model
    model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )
    # Data augmentation
    datagen = ImageDataGenerator(
        rotation_range=10,
        zoom_range=0.1,
        width_shift_range=0.1,
        height_shift_range=0.1,
    )

    # Fit the model with data augmentation
    datagen.fit(X_train)

    # Display the model structure
    model.summary()

    # Train the model with data augmentation
    model.fit(
        datagen.flow(X_train, y_train, batch_size=64),
        epochs=2,
        validation_data=(X_val, y_val),
    )

    model.evaluate(X_test, y_test)

    return model
