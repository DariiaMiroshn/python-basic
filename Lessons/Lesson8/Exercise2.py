"""Ваше завдання – написати функцію is_palindrome,
яка перевірятиме, чи є рядок паліндромом.
Паліндромом - це такий рядок, який читається
однаково зліва направо із права наліво без урахування
знаків пунктуації та розмірності букв.
Функція приймає на вхід рядок, та повертає булеве значення True або False
Приклад:

def is_palindrome(text):
    pass
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

"""

def is_palindrome(text):

    text = text.lower()
    result = ""
    for i in text:
        if i.isalnum():
            result += i
    print(result)
    return result == result[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
