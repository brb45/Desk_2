class Animal:
    _number_of_legs = 0
    _pairs_of_eyes = 0

    def __init__(self, age):
        self._age = age
        print("Animal created")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def print_legs_and_eyes(self):
        print("I have " + str(self._number_of_legs) + " legs and " \
              + str(self._pairs_of_eyes * 2) + " eyes.")

    def print_age(self):
        print("I am " + str(self._age) + " years old.")

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age


class Mammal(Animal):
    _pairs_of_eyes = 1

    def __init__(self, age, is_pregnant = False):
        super().__init__(age)
        self._is_pregnant = is_pregnant
        print("Mammal created")

    @property
    def is_pregnant(self):
        return self._is_pregnant

    @is_pregnant.setter
    def is_pregnant(self, is_pregnant):
        self._is_pregnant = is_pregnant


class DomesticMammal(Mammal):
    def __init__(self, name, age, favorite_toy, is_pregnant=False):
        super().__init__(age, is_pregnant)
        self._name = name
        self._favorite_toy = favorite_toy
        print("DomesticMammal created")

    @property
    def name(self):
        return self._name

    @property
    def favorite_toy(self):
        return self._favorite_toy

    @favorite_toy.setter
    def favorite_toy(self, favorite_toy):
        self._favorite_toy = favorite_toy

    @name.setter
    def name(self, name):
        self._name = name

    def talk(self):
        print(self._name + ": talks")

class Dog(DomesticMammal):
    _number_of_legs = 4
    # dog only
    _breed = "Just a dog"
    _breed_family = "Dog"

    def __init__(self, name, age, favorite_toy, is_pregnant=False):
        # DomesticMammal
        super().__init__(name, age, favorite_toy, is_pregnant)
        print("Dog created")

    def bark(self, times=1, other_domestic_mammal=None, is_angry=False):
        message = self.name
        if other_domestic_mammal is not None:
            message += " to " + other_domestic_mammal.name + ": "
        else:
            message += ": "
        if is_angry:
            message += "Grr "
        message += "Woof " * times
        print(message)

    def talk(self):
        self.bark()

    # objects can call classmethod too.
    @classmethod
    def print_breed(cls):
        print(cls._breed)

    @classmethod
    def print_breed_family(cls):
        print(cls._breed_family)


class TerrierDog(Dog):
    _breed = "Terrier dog"
    _breed_family = "Terrier"

    def __init__(self, name, age, favorite_toy, is_pregnant=False):
        super().__init__(name, age, favorite_toy, is_pregnant)
        print("TerrierDog created")


class SmoothFoxTerrier(TerrierDog):
    _breed = "Smooth Fox Terrier"

    def __init__(self, name, age, favorite_toy, is_pregnant=False):
        super().__init__(name, age, favorite_toy, is_pregnant)
        print("SmoothFoxTerrier created")



#_____________________________________________________________
from log_test import *


## calling
age = 40
# animal = Animal(age)
# animal_a = Animal(160)
# Animal created

# print(animal.age) # 40
# animal.age = 100
# print(animal.age) # 100

# if animal < animal_a:
#     print(True)
# else:
#     print(False)
# False

print("Mammal()____________________________")
# mammal_a = Mammal(15, True)
# Mammal created


print("DomesticMammal()____________________________")
# name, age, favorite_toy, is_pregnant=False
# d_mammal = DomesticMammal("Horse", 5, "Rubber", True)
# Animal created
# Mammal created
# DomesticMammal created

print("Dog()____________________________")
dog = Dog("Totia", 1, "bone", True)
# Dog created
dog.print_breed() # Just a dog
Dog.print_breed() # Just a dog


#_____________________________________________________________








#SmoothFoxTerrier.print_breed()
#SmoothFoxTerrier.print_breed_family()


tom = SmoothFoxTerrier("Tom", 5, "Sneakers")
print("____________________________________")
# Animal created
# Mammal created
# DomesticMammal created
# Dog created
# TerrierDog created
# SmoothFoxTerrier created

# print(isinstance(tom, Animal))
# print(isinstance(tom, Mammal))
# print(isinstance(tom, DomesticMammal))
# print(isinstance(tom, Dog))
# print(isinstance(tom, TerrierDog))
# print(isinstance(tom, SmoothFoxTerrier))
print("====================================")
# True
# # True
# # True
# # True
# # True
# # True

pluto = SmoothFoxTerrier("Pluto", 6, "Tennis ball")
print("....................................")
goofy = SmoothFoxTerrier("Goofy", 8, "Soda bottle")
print("************************************")
print(tom > pluto)
print(tom < pluto)
# print(goofy >= tom)
# print(tom <= goofy)
#
# tom.bark()
# tom.bark(2)
# tom.bark(2, pluto)
# tom.bark(3, pluto, True)
