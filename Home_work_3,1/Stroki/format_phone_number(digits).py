def format_phone_number(digits):
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
print(format_phone_number("9994432311"))