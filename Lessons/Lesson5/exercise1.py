
"""Користувач уводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
Змінна не може:
починатись із цифри
містити великі літери,
пробіл і знаки пунктуації (узяти можна тут string.punctuation), окрім нижнього підкреслення "_",
бути жодним із зареєстрованих слів.
При цьому повне ім'я змінної повинно складатися не більш чим з одного нижнього підкреслення "_".
Список зареєстрованих слів можна взяти із keyword.kwlist.

У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))

_ => True
__ => False
___ => False
x => True
get_value => True
get value => False
get!value => False
some_super_puper_value => True
Get_value => False
get_Value => False
getValue => False
3m => False
m3 => True
assert => False
assert_exception => True
"""

import string
import keyword

user_input = input("Enter name variable: ")
is_valid = True

forbidden_punctuation = []
for i in string.punctuation:
    if i != "_":
        forbidden_punctuation.append(i)
forbidden_punctuation.append(" ")

if not user_input:
    is_valid = False
else:
    if user_input[0].isdigit():
        is_valid = False

    if user_input != user_input.lower():
        is_valid = False

    for char in user_input:
        if char in forbidden_punctuation:
            is_valid = False

    if user_input in keyword.kwlist:
        is_valid = False

    if user_input.replace("_", "") == "" and len(user_input)> 1:
        is_valid = False


print(is_valid)
