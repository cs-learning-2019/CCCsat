list_of_num = [2, 1, 2, 3, 3, 99, 99]

# Loop over list of nums to populate dups
dups = {}
for num in list_of_num:
    if num in dups:
        dups[num] = dups[num] + 1
    else:
        dups[num] = 1

# Loop over dups and see if we have duplicates
for key in dups:
    value = dups[key]
    if value > 1:
        print("The number " + str(key) + " came up " + str(value) + " times.")
