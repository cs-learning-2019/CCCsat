binary_string = "011111011110"

def question2 (bs):
    counter = 0
    
    for bit in bs:
        if bit == "1":
            counter += 1
        else:
            if counter == 4:
                return True
            else:
                counter = 0

    if counter == 4:
        return True
    else:
        return False

print(question2(binary_string))
