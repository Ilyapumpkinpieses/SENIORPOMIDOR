def generate_squares(n):
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares
print(generate_squares(6))