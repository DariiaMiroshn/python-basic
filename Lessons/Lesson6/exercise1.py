"""Користувач уводить через дефіс дві літери,
Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
Жодних перевірок на помилку робити не треба, мінімальне значення
завжди менше або дорівнює максимальному.
Підказка: Використовуйте модуль string, у якому є string.ascii_letters,
з усім набором потрібних букв
Приклад:
"a-c" -> abc
"a-a" -> a
"s-H" -> stuvwxyzABCDEFGH
"a-A" -> abcdefghijklmnopqrstuvwxyzA
"""
import string

user_input = list(input("Enter range of letters: "))

letters_list = string.ascii_letters
letters_from_user = []

for i in user_input:
    if i.isalpha():
        letters_from_user.append(i)

print(letters_from_user)

index_element = []
for i in user_input:
    if i in letters_list:
        index_element.append(letters_list.index(i))
print(index_element)

fist_element = index_element[0]
last_element = index_element[-1]
print(fist_element, last_element)

print(letters_list[fist_element:last_element+1])