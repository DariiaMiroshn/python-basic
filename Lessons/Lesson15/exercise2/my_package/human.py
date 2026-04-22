class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"First name: {self.first_name}, last name: {self.last_name}, age: {self.age}, gender: {self.gender}"

    def show(self):
        return self.__str__()