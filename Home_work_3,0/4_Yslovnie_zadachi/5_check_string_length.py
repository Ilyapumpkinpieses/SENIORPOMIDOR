def check_string_length(string, length=5):
    if len(string) > length :
        print(f"Длина строки достаточная")
    else:
        print(f"Строка слишком короткая")
check_string_length("Python")
check_string_length("Hi")
check_string_length("Aloha")