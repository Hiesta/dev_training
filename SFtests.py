from math import pi


class Rectangle:
    def __init__(self, side_a, side_b):
        self.a = side_a
        self.b = side_b

    def get_area(self):
        return self.a * self.b

    def __eq__(self, other):
        return self.a * self.b == other.a * other.b

    def __str__(self):
        return f'class Rectangle, (x,y) = {self.a, self.b}'


class Square:
    def __init__(self, side):
        self.side = side

    def get_square_area(self):
        return self.side ** 2

    def __eq__(self, other):
        return self.side ** 2 == other.side ** 2

    def __str__(self):
        return f'class Square, side = {self.side}'


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circle_area(self):
        return round(pi * self.radius ** 2, 1)

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'class Circle, radius = {self.radius}'


class Triangle:
    def __init__(self, a, base, c, h):
        self.a = a
        self.base = base
        self.c = c
        self.h = h

    def get_triangle_area(self):
        return self.base * self.h / 2

    def __str__(self):
        return f'class Triangle, (a,b,c) = {self.a, self.base, self.c}'


class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.city = city
        self.surname = surname
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Balance: {self.balance} $'

    def get_info(self):
        return f'{self.name, self.surname, self.city}'


class StaticSquare:
    def __init__(self, side):
        self.side = side
        self.session_id = None
        self.client_ip = None
        self.console_log = None

    def __str__(self):
        return f'class StaticSquare, side = {self.side}'

    def get_area(self):
        return self.side


class SquareFactory:  # TODO: create method resolution
    @staticmethod
    def get_square(side):
        return StaticSquare(side * side)


class DogDecorations:
    _remainingTime = -1

    def __init__(self, age, gender, name):
        self.age = age
        self.gender = gender
        self.name = name

    @property
    def remaining_time(self):
        return self._remainingTime

    @remaining_time.setter
    def remaining_time(self, temp_age):
        if 25 - temp_age > 0:
            self._remainingTime = 25 - temp_age
        else:
            raise ValueError("There are no animals over 25 years")


dog_tester = DogDecorations(12, 'Male', "George")
dog_tester.remaining_time = 20
print(dog_tester.remaining_time)