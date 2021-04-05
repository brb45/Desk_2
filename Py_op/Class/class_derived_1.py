# _____________________________________________________
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages


class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_


ebook = Ebook("Python", "Packet", 500, "PDF")
# print(ebook.title, ebook.publisher, ebook.pages, ebook.format_)  #Python Packet 500 PDF

# _____________________________________________________
class Book1:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages


class Ebook1(Book1):
    def __init__(self, title, publisher, pages, format_):
        super().__init__(title, publisher, pages)
        self.format_ = format_

ebook1 = Ebook1("Python", "Packet", 500, "PDF")
# print(ebook1.title, ebook1.publisher, ebook1.pages, ebook1.format_) # Python Packet 500 PDF

# _____________________________________________________
####

## calling base class init
class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

class ElectricCar(Car):

    def __init__(self, battery_type, model, color, mpg):
        self.battery_type=battery_type
        super().__init__(model, color, mpg)