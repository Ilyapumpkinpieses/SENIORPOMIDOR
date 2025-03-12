name=input("Введите Ваше имя:")
experience_years= input("Сколько лет работаете в тестировщиком?:")
question =("Что такое переменная?")
print(question)
answer =input ("Ваш ответ: ")
if answer == "это именованная область памяти":
    print(f"Привет, {name}! Добро пожаловать в мир Python для тестировщиков.")
else :
    print(f"Привет, {name}! Ответ неверный.")