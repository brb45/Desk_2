class Base(object):
    def __init__(self):
        print("initializing Base")


class ChildA(Base):
    def __init__(self):
        print("initializing ChildA")
        super().__init__()


class ChildB(Base):
    def __init__(self):
        print("initializing ChildB")
        super().__init__()


class Grandchild(ChildA, ChildB):
    def __init__(self):
        print("initializing Grandchild")
        super().__init__()


Grandchild()

# In the case of multiple inheritance, you normally want to call the initializers of both parents,
# not just the first. Instead of always using the base class, super() finds the class
# that is next in Method Resolution Order (MRO), and returns the current object as an instance of that class.

# initializing Grandchild
# initializing ChildA
# initializing ChildB
# initializing Base