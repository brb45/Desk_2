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

    @classmethod
    def print_breed(cls):
        print(cls._breed)

    @classmethod
    def print_breed_family(cls):
        print(cls._breed_family)


class Anim:

    _class_legs = 4

    def __init__(self, name,num):
        self._name = name
        self._legs = num
        print("Created")

    @property
    def num_of_legs(self):
        return self._legs

    @num_of_legs.setter
    def num_of_legs(self, num):
        self._legs = num

    def __lt__(self, other):
        return self._legs < other._legs


print(Anim._class_legs)

my_dog = Anim("Churc", 4)


# calling property
print(my_dog.num_of_legs)

# calling setters
my_dog.num_of_legs = 100
print(my_dog.num_of_legs)

my_dog = Anim("Churc", 100)
my_dog1 = Anim("Churpc", 400)


print(my_dog.__lt__(my_dog1)) # True

print(my_dog < my_dog1)  # True