import random
# int - integer целое число
# str - string строка

random_num = random.randint(1, 100)
attempts = 10

print("Вітаю! Я загадав число від 1 до 100🕴.")
print("У вас є десять спроб до фатальної цифрової помилки 😜")

while True:
    num = int(input("\nвведите число: "))
    attempts -= 1
    print("осталось попыток", attempts)
    if num < random_num:
        print("загад число больше.")
    elif num > random_num:
        print("загад число меньше.")
    else:
        print("угадал:)")
        break

    if attempts == 0:
        print("бабах!!!!!!!!")
        break
