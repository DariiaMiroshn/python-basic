"""1. Квадрат числа.
Користувач уводить число. Програма виводить його квадрат.
Приклад:
Введіть число: 5
Квадрат числа: 25"""

# number = int(input("Enter number:"))
# result = number * number
# print(f"Square of {number} is {result}")

"""2. “Середнє трьох чисел”
Програма запитує три числа й виводить їх середнє арифметичне.
Приклад:
Введіть три числа: 2, 4, 6
Середнє: 4.0"""

# numbers1 = (int(input("Enter first number: ")))
# numbers2 = (int(input("Enter second number: ")))
# numbers3 = (int(input("Enter third number: ")))
# result = (numbers1 + numbers2 + numbers3) / 3
# print(f"Average:{result}")

"""3. “Перетворення хвилин у години”
Користувач уводить кількість хвилин. Програма виводить, скільки це годин і хвилин.
Приклад:
Введіть кількість хвилин: 135
2 години 15 хвилин"""

# amount_of_minutes = (int(input("Enter amount of minutes: ")))
# result = amount_of_minutes/60
# print(f"{amount_of_minutes} minutes is {amount_of_minutes//60} hours and {amount_of_minutes%60} minutes")

"""4. “Розрахунок знижки”
Користувач уводить ціну товару та розмір знижки у %.
Програма виводить кінцеву ціну.
Приклад:
Введіть ціну: 1000
Введіть знижку (%): 15
Ціна зі знижкою: 850.0"""

# price = float(input("Enter price: "))
# discount = float(input("Enter discount (%): "))
# result = price - (price * discount/100)
# print(f"Price with discount: {result}")

"""5. “Остання цифра числа”
Користувач уводить ціле число, програма виводить його останню цифру.
Приклад:
Введіть число: 347
Остання цифра: 7"""

# number = int(input("Enter a three-digit number: "))
# result = number % 10
# print(f"The last digit is: {result}")

"""6. “Периметр прямокутника”
Користувач уводить довжину та ширину. Програма виводить периметр.
Приклад:
Введіть довжину: 5
Введіть ширину: 3
Периметр: 16"""

# length = int(input("Enter length of rectangle: "))
# width = int(input("Enter width of rectangle: "))
# result = (length + width) * 2
# print(f"Perimeter of rectangle is: {result}")

"""7. Виведення числа в стовпчик
Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, 
після чого друкує на екрані стовпчик цифр, з якого це число складається. 
Наприклад, користувач уводить 1234, а програма виводить:
1
2
3
4
Завдання необхідно вирішити, використовуючи методи поділу (підказка // і % або divmod). 
Виведення в стовпчик можна зробити за допомогою 4-х функцій print.
Користувач може ввести будь-яке 4 значне ціле число. 
Будь-яке 4-х значне число - це число, яке складається з 4-х цифр, 
де кожна цифра може бути від 0 до 9 включно.
Ваше рішення має це враховувати! Якщо користувач увів не ціле число, 
це проблема користувача, а не вашої програми.
Створюйте рішення, виходячи з того, що число ЗАВЖДИ 4-х значне."""

# number = int(input("Enter 4-digits number: "))
# first_digit = number //1000
# second_digit = number //100 %10
# third_digit = number//10 % 10
# fourth_digit = number % 10
# print(first_digit)
# print(second_digit)
# print(third_digit)
# print(fourth_digit)
