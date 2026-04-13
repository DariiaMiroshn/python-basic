"""Напишіть функцію-генератор prime_generator, яка повертатиме прості числа.
Верхня межа цього діапазону визначається параметром цієї функції.
Наприклад, виклик функції
list(prime_generator(10)) повинен відповідати послідовності із чисел [2, 3, 5, 7].
Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд
"""

import math
def prime_generator(end):

    for number in range(2, end+1):

        is_prime = True
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number



from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
