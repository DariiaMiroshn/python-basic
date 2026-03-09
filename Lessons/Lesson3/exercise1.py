"""Найпростіший калькулятор
Програма має виконувати прості математичні дії (+, -, *, /).
 Користувачеві пропонується по черзі ввести числа та дію над цими числами,
 а програма, виходячи з дії, обчислює та друкує результат.
Зробити перевірку на те, що при діленні дільник не дорівнює 0!"""

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
operator = input("Enter operator(+, -, *, /):")
if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "*":
    result = number1 * number2
    print(result)
elif operator == "/":
    if number2 == 0:
        print("Error: Division by zero!")
    result = number1 / number2
    print(result)
else:
    print("Error: Invalid operator!")
