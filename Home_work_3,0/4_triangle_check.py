def check_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        print('Треугольник с такими сторонами не может быть')
        return

    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or c == b:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')

a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))

check_triangle(a, b, c)