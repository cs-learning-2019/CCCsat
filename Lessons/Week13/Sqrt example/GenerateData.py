import math

# Open connection to csv files
trainFile = open("./data/train.csv", "w")
testFile = open("./data/test.csv", "w")

# Generate training data
trainFile.write("x,y\n")
for x in range(0, 5000):
    y = math.sqrt(x)
    trainFile.write(str(x) + "," + str(y) + "\n")

# Generate test data
testFile.write("x,y\n")
for x in range(5000, 6000):
    y = math.sqrt(x)
    testFile.write(str(x) + "," + str(y) + "\n")

# Close connection to csv files
trainFile.close()
testFile.close()