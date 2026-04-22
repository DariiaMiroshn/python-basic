from .human import Human
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

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        if isinstance(other, str):
            return str(self) == other
        return False

    def __hash__(self):
        return hash(str(self))