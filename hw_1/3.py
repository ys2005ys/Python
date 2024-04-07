''' Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)'''


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

# Генерация случайного числа
num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Угадайте число от", LOWER_LIMIT, "до", UPPER_LIMIT)

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input("Попытка №" + str(attempt) + ": Ваше предположение: "))
    
    if guess < num:
        print("Загаданное число больше.")
    elif guess > num:
        print("Загаданное число меньше.")
    else:
        print("Поздравляю! Вы угадали число!")
        break

if guess != num:
    print("Увы! Вы не угадали число. Загаданное число было:", num)
