import math

# Open connection to csv files
trainFile = open("./data/train.csv", "w")
testFile = open("./data/test.csv", "w")

# Generate training data
trainFile.write("x,y\n")
for x in range(0, 1500, 3):
    y = round(math.sqrt(x), 2)
    trainFile.write(str(x) + "," + str(y) + "\n")

# Generate test data
testFile.write("x,y\n")
for x in range(1, 1500, 3):
    y = round(math.sqrt(x), 2)
    testFile.write(str(x) + "," + str(y) + "\n")

# Close connection to csv files
trainFile.close()
testFile.close()