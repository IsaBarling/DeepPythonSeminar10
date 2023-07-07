"""
Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры 
для этого типа. Внутри класса создайте экземпляр на основе переданного типа и 
верните его из класса-фабрики.
"""

from Task6 import Fish, Bird, Mammal

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, age, *args):
        if animal_type == "Fish":
            return Fish(name, age, *args)
        elif animal_type == "Bird":
            return Bird(name, age, *args)
        elif animal_type == "Mammal":
            return Mammal(name, age, *args)
        else:
            raise ValueError("Invalid animal type")

# Пример использования класса-фабрики
animal_factory = AnimalFactory()

fish = animal_factory.create_animal("Fish", "Немо", 2, "оранжевый")
fish.swim()
fish.display_info()

print()

bird = animal_factory.create_animal("Bird", "Попугай", 5, 30)
bird.fly()
bird.display_info()

print()

mammal = animal_factory.create_animal("Mammal", "Лев", 7, "саванна")
mammal.walk()
mammal.display_info()
