def check_grade(score):

    if score < 0 or score > 100:
        return "Ошибка,  допустимый диапазон от 0 до 100."
    if 90 <= score <= 100:
        return ("Отлично.")
    elif 75 <= score < 90:
        return ("Хорошо")
    elif 50 <= score < 75:
        return ("Удовлетворительно.")
    else:
        return ("Неудовлетворительно.")
score = int(input("Введите колчество баллов: "))
grade = check_grade(score)
print(f"Оценка за {score} баллов {grade} ")