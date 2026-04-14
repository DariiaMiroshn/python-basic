"""Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину).
Як поля товару можете використовувати значення ціни, опис, габарити товару.
Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
Створіть клас "Покупець". Як поля можна використовувати прізвище,
ім'я, по батькові, мобільний телефон і т.д.
Створіть клас "Замовлення". Замовлення може містити кілька товарів,
 причому кількість кожного з товарів може бути різною. Замовлення має
  бути "підв'язане" до користувача, який його здійснив. Реалізуйте
  метод обчислення сумарної вартості замовлення. Визначте метод
  str() для коректного виведення інформації про це замовлення."""

class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"Product name: {self.name}, price: {self.price}, description: {self.description}, dimensions: {self.dimensions}"

class User:

    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"User: {self.name}, surname: {self.surname}, phone_number: {self.phone_number}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, count):
        self.products[item] = count

    def __str__(self):
        total_items= ""
        for product, count in self.products.items():
            total_items += f"\n{product.name}: {count}pcs."
        return f"User: {self.user}\nItems: {total_items}"

    def get_total(self):
        total_price = 0
        for product, count in self.products.items():
            total_price += (product.price * count)
        return total_price


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
