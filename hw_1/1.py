
def check_triangle(a, b, c):

    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            return "Треугольник равносторонний"
        elif a == b or a == c or b == c:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"
    else:
        return "Треугольник с такими сторонами не существует"
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

result = check_triangle(a, b, c)
print(result)
