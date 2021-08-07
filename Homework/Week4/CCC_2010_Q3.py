# CCC 2010 J3 Punchy

var = {"A" : 0, "B" : 0}

while(True):
    line = input().split()
    if line[0] == "1":
        var[line[1]] = int(line[2])
    elif line[0] == "2":
        print(int(var[line[1]]))  # On the CCC convert into int just to be sure
    elif line[0] == "3":
        var[line[1]] = var[line[1]] + var[line[2]]
    elif line[0] == "4":
        var[line[1]] = var[line[1]] * var[line[2]]
    elif line[0] == "5":
        var[line[1]] = var[line[1]] - var[line[2]]
    elif line[0] == "6":
        var[line[1]] = int(var[line[1]] / var[line[2]])
    elif line[0] == "7":
        break
