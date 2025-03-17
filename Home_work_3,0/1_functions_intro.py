def greet_user(name):
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}! Добро пожаловать в мир Python!")

def calculate_sum(a, b):
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    summ = a + b
    print(f"Сумма чисел: {summ}")

greet_user("name")
calculate_sum("a", "b")