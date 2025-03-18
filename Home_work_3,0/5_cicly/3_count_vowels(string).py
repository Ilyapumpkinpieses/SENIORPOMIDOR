def count_vowels(string):
    vowels = "aeiouAEIOU"
    caunt = 0
    for i in string:
        if i in vowels:
            caunt += 1
    print(f"Количество гласных в строке '{string}': {caunt}")
    return caunt

count_vowels("Hello World!")