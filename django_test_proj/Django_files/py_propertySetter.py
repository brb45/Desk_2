# @property decorator is a built-in decorator in Python for the property() function.
class person:
    def __init__(self):
        self.__name=''
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value

    @name.deleter
    def name(self, value):
        print('Deleting..')
        del self.__name

# >>> p=person()
# >>> p.name='Steve'
# >>> p.name
# Steve
# >>> del p.name
# Deleting..



class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' '+ self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

# Init a Person
person = Person('selva', 'prabhakaran')
print(person.fullname)  #> selva prabhakaran
print(person.first)  #> selva
print(person.last)  #> prabhakaran

# Setting fullname calls the setter method and updates person.first and person.last
person.fullname = 'velu pillai'

# Print the changed values of `first` and `last`
print(person.fullname) #> velu pillai
print(person.first)  #> pillai
print(person.last)  #> pillai



##############
class AwwYeah:

    def __init__(self):
        self._bar = ''

    @property
    def foo(self):
        return 'More awesome please: {}'.format(self._bar)

    @foo.setter
    def foo(self, value):
        self._bar = '{} is great.'.format(value)

# >>> a = AwwYeah()
# >>> a.foo = 'Python'
# >>> a.foo
# 'More awesome please: Python is great.'

#########
def display(str):
    print(str)

# decorator
def display_decorator(fn):
    def display_wrapper(str):
        print("Output: ", end=" ")
        fn(str)
    return display_wrapper

output = display_decorator(display)
str = "Hello Testing"
output(str)
# Output:  Hello Testing

##

def display1_decorator(fn):
    def display1_wrapper(str):
        print("Output: ", end=" ")
        fn(str)
    return display1_wrapper

@display1_decorator
def display1(str):
    print(str)

# decorator
display1("Using @decorator")














