def get_unique_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {char.lower() for char in s if char.lower() in vowels}
print(get_unique_vowels("Hello World"))