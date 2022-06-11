import numpy as np

# Open connection to csv files
trainFile = open("./data/train.csv", "w")
testFile = open("./data/test.csv", "w")

# Generate training data
trainFile.write("x,y\n")
for i in range(10000):
    x = np.random.random() * 50
    y = x * x
    trainFile.write(str(x) + "," + str(y) + "\n")

# Generate test data
testFile.write("x,y\n")
for i in range(100):
    x = np.random.random() * 50
    y = x * x
    testFile.write(str(x) + "," + str(y) + "\n")

# Close connection to csv files
trainFile.close()
testFile.close()