number = int(input("Введите целое число: "))

hexadecimal = hex(number)[2:]  
print("Шестнадцатеричное представление числа:", hexadecimal)


hex_check = hex(number)[2:]  

if hexadecimal == hex_check:
    print("Результат верный.")
else:
    print("Результат неверный.")
