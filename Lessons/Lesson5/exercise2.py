"""Модифікувати калькулятор таким чином, щоб він працював доти,
доки користувач цього хоче. Тобто, потрібно робити запит
 до користувача на продовження роботи калькулятора
 після кожного обчислення - якщо користувач увів yes (можна просто y),
то нове обчислення, інакше - закінчення роботи."""

continue_working = "yes"
while continue_working == "yes" or continue_working == "y":

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

    continue_working = input("Enter yes/y to continue: ").lower()
