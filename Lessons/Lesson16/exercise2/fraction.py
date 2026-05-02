class Fraction:
    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError("Numerator  must be an integer")
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError("Denominator must be an integer")
        if value == 0:
            raise ValueError("Denominator cannot be zero")
        if value < 0:
            self.__numerator = self.__numerator * -1
            self.__denominator = abs(value)
        else:
            self.__denominator = value

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_num = self.numerator * other.denominator + other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Fraction(new_num, new_den)
        return False

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_num = self.numerator * other.denominator - other.numerator * self.denominator
            new_den = self.denominator * other.denominator
            return Fraction(new_num, new_den)
        return False

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_num = self.numerator * other.numerator
            new_den = self.denominator * other.denominator
            return Fraction(new_num, new_den)
        return False

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        return False

    def __str__(self):
        return f"Fraction: {self.__numerator}, {self.__denominator}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
