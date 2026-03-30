"""Напишіть функцію common_elements, яка згенерує два списки елементів
з генераторного виразу (range) для 100 елементів, за наступними правилом:
Один список із числами кратними 3, інший з кратними числами 5.
За допомогою множин створіть набір із числами, які є в обох множинах (перетин).
Функція повинна повернути цю множину як результат своєї роботи.

def common_elements():

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
"""


def common_elements():

    multiples_3 = [i for i in range (100) if i % 3 ==0]
    multiples_5 = [i for i in range (100) if i % 5 ==0]

    result = set(multiples_3) & set(multiples_5)
    return result

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print(common_elements())