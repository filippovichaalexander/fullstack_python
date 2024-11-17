# task 1
class MyTime:
    def __init__(self, *args):
        if len(args) == 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif len(args) == 1 and isinstance(args[0], str):
            h, m, s = map(int, args[0].split(":"))
            self.hours = h
            self.minutes = m
            self.seconds = s
        elif len(args) == 3 and all(isinstance(arg, int) for arg in args):
            self.hours, self.minutes, self.seconds = args
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            raise ValueError("Невепный вводные параметры")

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __ne__(self, other):
        return (self.hours, self.minutes, self.seconds) != (other.hours, other.minutes, other.seconds)

    def __gt__(self, other):
        return (self.hours, self.minutes, self.seconds) > (other.hours, other.minutes, other.seconds)

    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)

    def __ge__(self, other):
        return (self.hours, self.minutes, self.seconds) >= (other.hours, other.minutes, other.seconds)

    def __le__(self, other):
        return (self.hours, self.minutes, self.seconds) <= (other.hours, other.minutes, other.seconds)

    def convert_to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        if isinstance(other, MyTime):
            total_seconds = self.convert_to_seconds() + other.convert_to_seconds()
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return MyTime(hours, minutes, seconds)
        elif isinstance(other, (int, float)):
            total_seconds = self.convert_to_seconds() + other
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return MyTime(hours, minutes, seconds)
        else:
            raise TypeError("Неверный тип операнда")

    def __sub__(self, other):
        if isinstance(other, MyTime):
            total_seconds = self.convert_to_seconds() - other.convert_to_seconds()
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return MyTime(hours, minutes, seconds)
        elif isinstance(other, (int, float)):
            total_seconds = self.convert_to_seconds() - other
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return MyTime(hours, minutes, seconds)
        else:
            raise TypeError("Неверный тип операнда")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            total_seconds = self.convert_to_seconds() * other
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return MyTime(hours, minutes, seconds)
        else:
            raise TypeError("Неверный операнд")

# task 2

class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def display_speed(self):
        print(f"Скорость автомобиля: {self.__speed} км/ч")

    def reverse(self):
        self.__speed *= -1

# task 3

class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        length = len(s)
        if len(self) % length == 0:
            return self == s * (len(self) // length)
        return False

    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]

# определение объектов

s1 = SuperStr("abcabc")
print(s1.is_repeatance("abc"))
print(s1.is_palindrom())

s2 = SuperStr("abcba")
print(s2.is_palindrom())

s3 = SuperStr("")
print(s3.is_palindrom())