def merge_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result
print(merge_lists([4, 5, 7], [8, 5, 9]))