"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Создаем генератор
fib_gen = fibonacci_generator()

# Выводим первые 10 чисел Фибоначчи
for _ in range(10):
    print(next(fib_gen), end=" ")
