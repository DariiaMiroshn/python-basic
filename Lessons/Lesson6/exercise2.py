"""Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
Ну і додатковим завданням є турбота про виведення.
Слово "день" підбирається на основі кількості днів, а години,
хвилини і секунди повинні заповнюватися нулями при одноцифрових значеннях.

Підказка: одна хвилина - 60 сек, В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек.
Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти
відповідну кількість днів, годин, хвилин, а те що залишиться - це секунди, які менше 60 ;)
Доповнити провідними нулями можна за допомогою методу zfill(2)

Приклад:
0 -> 0 днів, 00:00:00
224930 -> 2 дні, 14:28:50
466289 -> 5 днів, 09:31:29
950400 -> 11 днів, 00:00:00
1209600 -> 14 днів, 00:00:00
1900800 - > 22 дні, 00:00:00
8639999 -> 99 днів, 23:59:59
22493 -> 0 днів, 06:14:53
7948799 -> 91 день, 23:59:59
"""

user_input = (int(input("Enter amount of seconds from 0 to 8639999: ")))

seconds_in_one_day = 60 * 60 * 24
seconds_in_one_hour = 60 * 60
seconds_in_one_minute = 60

days = user_input//seconds_in_one_day
remaining = user_input%seconds_in_one_day

hours = remaining//seconds_in_one_hour
remaining = remaining%seconds_in_one_hour

minutes = remaining//seconds_in_one_minute
remaining = remaining% seconds_in_one_minute

hours_f = str(hours).zfill(2)
minutes_f = str(minutes).zfill(2)
seconds_f = str(remaining).zfill(2)

remainder10 = int(days) % 10
remainder100 = int(days) % 100

if 11 <= remainder100 <= 14:
    word ="днів"

elif remainder10 == 1:
    word= "день"

elif 2 <= remainder10 <= 4:
    word = "дні"

else:
    word=("днів")

print(f"{days} {word}, {hours_f}:{minutes_f}:{seconds_f}")
