def question4(list_of_str):
    result = []

    for string in list_of_str:
        sub_list = list(string)
        result.append(sub_list)

    return result

print(question4(["jelly", "salty", "sweaty"]))
