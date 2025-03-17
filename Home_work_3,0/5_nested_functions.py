def calculator():
    num1 = float(input("Введите первое число: "))
    operation = input("Введите опрерацию (+ , - , / ,*):")
    num2 = float(input("Введите второе число: "))

    if operation  == "+":
        results = num1+num2
    elif operation == "-":
        results = num1-num2
    elif operation == "/":
        results = num1 / num2
    elif operation == "*":
        results = num1 * num2
    else:
        return "Ошибка: неизвестная операция!"
    return f"Результат: {results}"
print(calculator())