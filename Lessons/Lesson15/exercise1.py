"""
Модифікуйте клас Група (завдання минулої лекції) так,
щоб при спробі додавання до групи більше 10-ти студентів,
було порушено виняток користувача.

Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
І обробити його поза межами класу. Тобто. потрібно перехопити
цей виняток, при спробі додавання 11-го студента.
"""
class LimitError(Exception):
    def __init__(self, message = "In the group cannot be more than 10 students"):
        self.message = message
        super().__init__(self.message)


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


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, student_class):
        super().__init__(gender, age, first_name, last_name)
        self.student_class = student_class

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Class: {self.student_class}"

    def show(self):
        human_info = super().show()
        student_info = f"{human_info} student studied at {self.student_class} class."
        return student_info

    def compare(self, factor):
        if self.first_name == factor:
            return True
        if self.last_name == factor:
            return True
        else:
            return False



class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise LimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None


    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + "\n"
        return f'Number:{self.number}\n {all_students} '

students = [Student('Male', 30, 'Steve', 'Jobs', 'AN142'),
Student('Female', 25, 'Liza', 'Taylor', 'AN145'),
Student('Male', 23, 'Stas', 'Topolya', 'AN145'),
Student('Female', 22, 'Tanya', 'Lisova', 'AN145'),
Student('Male', 21, 'Orest', 'Zhuk', 'AN145'),
Student('Female', 26, 'Oksana', 'Sova', 'AN145'),
Student('Male', 28, 'Yuriy', 'Kolosok', 'AN145'),
Student('Female', 25, 'Svitlana', 'Lyalka', 'AN145'),
Student('Female', 35, 'Lina', 'Kostenko', 'AN145'),
Student('Female', 27, 'Alla', 'Kulyk', 'AN145'),
Student('Male', 24, 'Kyryl', 'Stepovuy', 'AN145')]

gr = Group('PD1')
try:
    for student in students:
        gr.add_student(student)
except LimitError as e:
    print(f"Error: {e}")

print(gr)
assert str(gr.find_student('Jobs')) == str(students[0]), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
