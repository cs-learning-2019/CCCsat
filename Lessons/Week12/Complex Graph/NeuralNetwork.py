"""
Source code and data is pulled from https://github.com/KeithGalli/neural-nets

Note: in the testing data 0 = Red and 1 = Blue
"""

# We will be using Keras which is an API using TensorFlow as its backend
# Think of Keras as a wrapper around TensorFlow that provides an easy to use functions to quickly build a neural net
from tensorflow import keras

# Used for parsing training and test data. In our case we have data in a CSV file and Pandas is great for this.
import pandas as pd

# Used for processing data and more generally for scientific computing and mathematical operations (Linear Algebra)
import numpy as np

# Parse the data into a data frame
training_data_df = pd.read_csv('./data/train.csv')

# Use numpy to shuffle the training data
# It is important to shuffle the data if the rows are not already randomized
np.random.shuffle(training_data_df.values)

# Define the neural network
# Sequential --> (feed forward) which means data moves through the layers of the network from left to right
# This is where we can adjust the hyper parameters like how many neurons there are in the hidden layers
# The input layer is not explicitly defined and we just provide an input shape into the first layer
# input_shape=(2,) means a single piece of input is a 1D numpy array with two values e.g. [2, 5]
model = keras.Sequential([
	keras.layers.Dense(256, input_shape=(2,), activation='relu'),
	keras.layers.Dropout(0.4),
	keras.layers.Dense(128, activation='relu'),
	keras.layers.Dropout(0.4),
	keras.layers.Dense(128, activation='relu'),
	keras.layers.Dense(2, activation='sigmoid')
])

# Compile the model (we still have to train it)
# Notice that we set from_logits=True. That is because we didn't apply a softmax activation function to the output layer
# Softmax basically makes it so that the output values are turned into probability 0-1 and the sum of values
# across all output neurons equals 1.
# If you are interested in what CategoricalCrossentropy is doing look here...
# https://stackoverflow.com/questions/65131391/what-exactly-is-kerass-categoricalcrossentropy-doing
# If you want more info on from_logits=True then go here
# https://datascience.stackexchange.com/questions/73093/what-does-from-logits-true-do-in-sparsecategoricalcrossentropy-loss-function
# If you want more info on the adam optimizer then go here
# https://keras.io/api/optimizers/adam/
model.compile(optimizer='adam', loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

# Stack the x and y data to form the full array of input training data
stacked_data = np.column_stack((training_data_df.x.values, training_data_df.y.values))

# Train the neural network
model.fit(stacked_data, training_data_df.color.values, batch_size=32, epochs=5)

# Parse the testing data (validation data)
test_data_df = pd.read_csv('./data/test.csv')

# Stack the x and y values just like with the training data
stacked_test_data = np.column_stack((test_data_df.x.values, test_data_df.y.values))

print("EVALUATION RESULT")
model.evaluate(stacked_test_data, test_data_df.color.values)

# Make a prediction
print("PREDICTION RESULT")
prediction = model.predict(np.array([[-4, -4]]))
classes = np.argmax(prediction, axis=1)
print(prediction)
print(classes)
