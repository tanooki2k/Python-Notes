from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @staticmethod
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    @property
    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    @property
    def num_legs(self):
        return 2


animals = [Dog('Fido'), Monkey('Jerry')]
for a in animals:
    print(isinstance(a, Animal))
    print(a.num_legs)
