"""
Neural network for predicting the square root of a positive number.

Author: Kavan Lam
Date: June 3, 2022
"""

from tensorflow import keras
import pandas as pd
import numpy as np

training_data_df = pd.read_csv('./data/train.csv')

# Numpy seems to not work for shuffling so we do it directly using the data frame
training_data_df = training_data_df.sample(frac=1).reset_index(drop=True)

# Define the neural network model and compile
# We do not want an activation function for the output layer
model = keras.Sequential([
    keras.layers.Dense(16, input_shape=(1,), activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the neural network
model.fit(np.reshape(training_data_df.x.values, (-1, 1)), training_data_df.y.values, batch_size=10, epochs=690)

print("EVALUATION RESULT")
test_data_df = pd.read_csv('./data/test.csv')
loss = model.evaluate(np.reshape(test_data_df.x.values, (-1, 1)), test_data_df.y.values)

# Make a prediction
print("PREDICTION RESULT")
prediction = model.predict(np.array([[4], [9], [16], [25], [36], [1], [2], [100], [1000], [50], [550]]))
print(prediction)