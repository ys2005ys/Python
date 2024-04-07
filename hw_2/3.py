from fractions import Fraction

fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

numerator1, denominator1 = fraction1.split('/')
numerator1 = int(numerator1)
denominator1 = int(denominator1)

numerator2, denominator2 = fraction2.split('/')
numerator2 = int(numerator2)
denominator2 = int(denominator2)

fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

sum_fraction = fraction1 + fraction2
multiplic_fraction = fraction1 * fraction2

print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", multiplic_fraction)
