# task 1

class InfiniteSequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        return result

def get_infinite_sequence(sequence):

    while True:
        for item in sequence: yield item

sequence = [1, 2, 3]
gen = get_infinite_sequence(sequence)
count = int(input("Введите количество чисел для вывода: "))

for _ in range(count): print(next(gen))


# task 2

class Pizza:
    def __init__(self, size=None, cheese=False, pepperoni=False,
                 mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        return f"Pizza size: {self.size}, Cheese: {self.cheese}, Pepperoni: {self.pepperoni}, Mushrooms: {self.mushrooms}, Onions: {self.onions}, Bacon: {self.bacon}"

class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        self.builder.set_size("Medium")
        self.builder.add_cheese()
        self.builder.add_pepperoni()
        self.builder.add_mushrooms()
        self.builder.add_bacon()
        return self.builder.build()

# Пример использования
builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)

# task 3

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Неизвестный тип животного")

class PizzaBuilder:
    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def build(self):
        return Pizza(self.toppings)

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def __str__(self):
        return f"Пицца с ингредиентами: {', '.join(self.toppings)}"

class PizzaMaker:
    def make_pizza(self, builder):
        builder.add_topping("Сыр")
        builder.add_topping("Томаты")
        builder.add_topping("Бекон")
        return builder.build()


factory = AnimalFactory()
dog = factory.create_animal("dog")
print(dog.speak())  # Вывод: "Гав!"

cat = factory.create_animal("cat")
print(cat.speak())  # Вывод: "Мяу!"

builder = PizzaBuilder()
pizza_maker = PizzaMaker()
pizza = pizza_maker.make_pizza(builder)
print(pizza)
