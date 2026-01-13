# 2.1
name = str(input('Введите ваше имя: '))
# 1. 
def greet(name):
    print(f"Привет, {name}!")
# 2. 
def square(num):
    return num ** 2
# 3. 
def max_of_two(a, b):
    return a if a > b else b
# Пример:
greet("Анна")                
print(square(5))             
print(max_of_two(10, 7))     
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

