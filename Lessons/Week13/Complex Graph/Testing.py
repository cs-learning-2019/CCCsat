"""
This is a testing file where you can print out how the data looks at different stages
and also gives you a place to experiment with Numpy and Pandas
"""

# Used for parsing training and test data. In our case we have data in a CSV file and Pandas is great for this.
import pandas as pd

# Used for processing data and more generally for scientific computing and mathematical operations (Linear Algebra)
import numpy as np

# Parse the data into a data frame
training_data_df = pd.read_csv('./data/train.csv')
print(training_data_df)

# We can look at the values attribute which is a 2D numpy array where each sublist holds the data for one row
print(training_data_df.values)


# Use numpy to shuffle the training data
np.random.shuffle(training_data_df.values)

# Print out the first few rows (the head of the data frame)
print(training_data_df.head())

# Collect the x and y values together
stacked_data = np.column_stack((training_data_df.x.values, training_data_df.y.values))
print(stacked_data)

# (20000, 2) = two dimensions. The first dimension is size 20000 (rows) and the second dimension is size 2 (cols)
print(stacked_data.shape)
print(stacked_data[0].shape)

# Get the values for the last column
print(training_data_df.color.values)

print("END OF TESTING FILE")
