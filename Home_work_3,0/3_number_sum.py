
def sum_numbers():
    n = int(input("Введите число: "))
    summ = 0
    for i in range(1, n + 1):
        summ += i
    print (f"Сумма чисел от 1 до {n}: {summ}")
    return summ
sum_numbers()

