def group_by_first_letter(strings):
    result = {}

    for string in strings:
        first_char = string[0].lower() if string else ''
        if first_char not in result:
            result[first_char] = []
        result[first_char].append(string)
    return result
strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))