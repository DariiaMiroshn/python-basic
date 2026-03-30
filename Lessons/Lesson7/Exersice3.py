"""Функція second_index приймає як параметри 2 рядки.
Вам необхідно знайти індекс другого входження шуканого рядка в рядку для пошуку.
Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims".
Якби нам треба було знайти її перше входження, то тут усе просто:
за допомогою функції index або find ми можемо дізнатися,
 що "s" - це перший символ у слові "sims",
а значить індекс першого входження дорівнює 0.
Але нам Необхідно визначити другу "s", а вона четверта за рахунком.
Отже, індекс другого входження (і у відповідь питання) дорівнює 3.
Рядок, який потрібно знайти, може складатися з кількох символів.
Input: Два рядки (String).
Output: Int or None

Приклади:
def second_index(text, some_str):
  pass
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
"""

def second_index(text: str, some_str: str):

    first = text.find(some_str)
    if first == -1:
        return None
    second = text.find(some_str, first + 1)

    if second == -1:
        return None
    else:
        return second

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')