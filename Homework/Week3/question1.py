# Determine how many names have a length greater than 4 and contains no a, b or c
grade_to_names = {1: ["bob", "ceb", "Tonoro", "John"], 2: ["Kavanny", "Jacmmmy", "zed"], 3: ["Windows", "Zemmky"]}

count = 0

for grade in grade_to_names:
    for name in grade_to_names[grade]:
        if len(name) > 4 and not ("a" in name) and not ("b" in name) and not ("c" in name):
            count += 1

print(count)
