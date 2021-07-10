def question3 (input_string):
    new_string = ""

    for character in input_string:
        if character.isdigit():
            new_string += str((int(character) + 1) % 10)
        else:
            if character == "z":
                new_string += "a"
            elif character == "Z":
                new_string += "A"
            else:
                new_string += chr(ord(character) + 1)

    return new_string

print(question3("970abcBNQZz2"))
