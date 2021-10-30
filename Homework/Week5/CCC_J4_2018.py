# CCC 2018 J4 Sunflowers
# Kavan Lam
# Oct 23, 2021

# Get inputs
N = int(input())

data = []
for i in range(N):
    row = input().split(" ")
    data.append([int(num) for num in row])

# Define helper function to check if a given orientation is correct
def check_data(data):
    # Check each data point
    for row in range(N):
        for col in range(N):
            current_value = data[row][col]
            
            # Get the right data point
            right_value = -99
            if col + 1 < N:
                right_value = data[row][col + 1]
                
            # Get the bottom data point
            bottom_value = -99
            if row + 1 < N:
                bottom_value = data[row + 1][col]

            # For each point the right and bottom data must be larger
            if (current_value > right_value and right_value != -99) or (current_value > bottom_value and bottom_value != -99):
                return False
            
    # If we get here then the data is good
    return True

# Define a helper function to rotate the data matrix by 90 degrees
# We will turn all rows into columns and then reverse all rows.
# Doing this gives a rotation of 90 degress counter clockwise
def rotate_data(data):
    new_data = [row.copy() for row in data]

    # First turn all rows in columns
    col_index = 0
    for row in data:
        for row_index in range(N):
            new_data[row_index][col_index] = row[row_index]
        col_index += 1

    # Reverse all rows
    new_data = [row[::-1] for row in new_data]

    # Return the new data
    return new_data

# Define a helper function to print the data
def print_data(data):
    row_data = ""
    for row in data:
        for num in row:
            row_data += str(num) + " "
        print(row_data[0:-1])
        row_data = ""
        
# Determine the original data
if check_data(data) == True:
    print_data(data)
else:
    for i in range(3):
        data = rotate_data(data)
        if check_data(data) == True:
            print_data(data)
            break





        





    
    

























