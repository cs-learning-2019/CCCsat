from tensorflow import keras
import numpy as np

model = keras.models.load_model("square_num_model")
print("PREDICTION RESULT")
prediction = model.predict(np.array([[10], [20], [30], [7], [15]]))
print(prediction)