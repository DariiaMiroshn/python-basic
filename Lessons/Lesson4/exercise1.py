"""Написати програму, яка переміщає всі нулі в кінець списку.
Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
Порядок ненульових чисел має зберегтися!"""
"""
[0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
[0] -> [0]
[1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
"""

# numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# zero_count = numbers.count(0)
# print(zero_count)
#
# new_numbers = []
# for i in numbers:
#     if i != 0:
#         new_numbers.append(i)
# print(new_numbers)
#
# for i in range(zero_count):
#     new_numbers.append(0)
#
# print(new_numbers)


numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
zero_count = numbers.count(0)
for i in range (zero_count):
        numbers.remove(0)
print(numbers)

for i in range(zero_count):
        numbers.append(0)
print(numbers)