def find_min(numbers):
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    print(f"Минимальное число в списке:", {min})
    return min

find_min([7, 22, 66, 6565, 5])