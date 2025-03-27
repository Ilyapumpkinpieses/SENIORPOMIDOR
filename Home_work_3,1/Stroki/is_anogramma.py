
def is_anagram(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    return sorted(s1) == sorted(s2)


s1 = input("Введите s1: ").lower()
s2 = input("Введите s2: ").lower()
print(is_anagram(s1, s2))