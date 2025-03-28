def merge_dicts(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 7, "a": 2}

print(merge_dicts(dict1, dict2))