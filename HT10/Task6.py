'''
Задание №6
📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс
Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.
'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age} лет")


class Fish(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def swim(self):
        print(f"{self.name} плывет по воде.")

    def display_info(self):
        super().display_info()
        print(f"Цвет: {self.color}")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} летит по воздуху.")

    def display_info(self):
        super().display_info()
        print(f"Размах крыльев: {self.wingspan} см")


class Mammal(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def walk(self):
        print(f"{self.name} идет по земле.")

    def display_info(self):
        super().display_info()
        print(f"Вид: {self.species}")


fish = Fish("Немо", 2, "оранжевый")
fish.swim()
fish.display_info()

print()

bird = Bird("Попугай", 5, 30)
bird.fly()
bird.display_info()

print()

mammal = Mammal("Лев", 7, "саванна")
mammal.walk()
mammal.display_info()
