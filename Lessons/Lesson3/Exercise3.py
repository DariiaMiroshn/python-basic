"""Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
Тобто, у результаті повинен вийти список із 2-х списків.
Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
у списку парна кількість елементів і в списку непарна кількість елементів.
"""
from os.path import split

numbers = list(input("Enter your list here: ").split())
length = len(numbers)
middle = (length+1)//2
first_half_of_numbers_list = numbers[: middle]
second_half_of_numbers_list = numbers[middle :]
renewed_numbers = [first_half_of_numbers_list, second_half_of_numbers_list]
print(f"Numbers list is: numbers = {numbers}")
print(f"Renewed number list is: renewed_numbers = {renewed_numbers}")


