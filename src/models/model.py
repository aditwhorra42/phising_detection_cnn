"""
Create CNN model.
"""
import pickle
from typing import Any, Dict
from keras.models import Sequential
from keras.layers import Embedding, Conv1D, MaxPooling1D, Flatten, Dense, Dropout


def build_cnn_model(params: Dict[str, Any]) -> Sequential:
    """Builds the CNN model for phissing detection.

    Args:
        params (Dict[str, Any]): The laoded training parameters

    Returns:
        Sequential: Returns the keras sequential model.
    """

    model = Sequential()

    with open("data/tokenized/char_index.pkl", 'rb') as file:
        char_index = pickle.load(file)

    voc_size = len(char_index.keys())
    print(f"voc_size: {voc_size}")

    model.add(Embedding(voc_size + 1, 50))

    model.add(Conv1D(128, 3, activation="tanh"))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 7, activation="tanh", padding="same"))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 5, activation="tanh", padding="same"))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation="tanh", padding="same"))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 5, activation="tanh", padding="same"))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation="tanh", padding="same"))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation="tanh", padding="same"))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Flatten())

    model.add(Dense(len(params["categories"]) - 1, activation="sigmoid"))

    print("Model Ready...")
    return model
