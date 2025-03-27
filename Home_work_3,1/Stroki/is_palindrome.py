import re
def is_palindrome (s):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))                     