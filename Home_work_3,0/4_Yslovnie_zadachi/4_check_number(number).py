def check_number(number):
    if number > 0:
        if number % 2 == 0:
            print(f"Число {number} положительное и чётное.")
        else:
            print(f"Число {number} чётное,но не положительное.")
        if number % 2 != 0:
            print(f"Число {number} положительное и нечетное")
    else:
        print(f"Число {number} отрицательное.")
check_number(5)