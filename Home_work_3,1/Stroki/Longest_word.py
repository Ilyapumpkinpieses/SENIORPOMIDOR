def longest_word(s):
    words = s.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word("I love big brother"))