# 2.1
name = str(input('Введите ваше имя: '))
age = input('Введите Ваш возраст: ')
def describe_person(name, age = 30):
    return f'Меня зовут {name}, мне {age} лет'
    if age:
        return (describe_person(name, age))
    else:
       print(describe_person(name))

# 2.2

from math import sqrt

number = int(input('Введите простое число: '))
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
if is_prime(number):
    print('Число простое')
else:
    print('Число не простое')

#2.3
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Пример:
print(is_prime(17))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
