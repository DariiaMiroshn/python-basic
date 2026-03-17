"""1. Необхідно створити список випадкових чисел із випадковою кількістю елементів від 3 до 10.
2. Створить інший список з 3 елементів зі списку з п.1 - першим, третім і другим з кінця.
Приклад того, як має виглядати фінальний список:

[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
[1, 1, 2, 1] == [1, 2, 2]
[6, 3, 7] == [6, 7, 3]
"""
import random

# length = random.randint(3,10)
# numbers = []
#
# for i in range(length):
#     number = random.randint(1, 100)
#     numbers.append(number)

# print(numbers)

numbers = [random.randint(1, 10) for i in range(random.randint(3, 10))]
print(numbers)

new_numbers = [numbers[0], numbers[2], numbers[-2]]
print(new_numbers)









