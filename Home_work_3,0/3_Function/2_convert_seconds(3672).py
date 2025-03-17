t = int(input("Введите количество секунд: "))
def convert_seconds(t):

    minutes = (t // 60) % 60
    hours = t // 3600
    if (t % 60) > 0:
        minutes += 1

    print(f"В {t} секундах содержится {hours} час(ов) и {minutes} минут(ы).")
    return hours, minutes

convert_seconds(t)