def extract_subdict(my_dict, keys):
    return {key: my_dict[key] for key in keys if key in my_dict}
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}