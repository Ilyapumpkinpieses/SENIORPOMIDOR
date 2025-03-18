def count_items(*args):
    count = len(args)
    print(f"Количество переданных элементов: {count}")

count_items("apple", "banana", "cherry")