data = open("input.txt", "r")

first_name = []
last_name = []

for line in data:
    better_line = line.strip()
    split_version = better_line.split(" ")
    first_name.append(split_version[0])
    last_name.append(split_version[1])

print(first_name)
print(last_name)
