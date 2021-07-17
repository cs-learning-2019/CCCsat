names = ["Kelly", "John", "Kevin", "Tony", "Jack", "Wilson", "Tina", "Cab"] # 8 names
ages = [7, 5, 6, 8, 7, 6, 5, 7]

output = {}

for index in range(0, len(names)):
    # Extract the data
    name = names[index]
    age = ages[index]

    # Put the data into the dictonary
    if age in output:
        output[age].append(name)
    else:
        output[age] = [name]


print(output)
