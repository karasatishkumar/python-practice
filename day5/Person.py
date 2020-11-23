class Person:

    def __init__(self, name, loc, age):  # parameterized CTOR
        print("I AM BORN.....")
        self.name = name
        self.loc = loc
        self.age = age

    def convert(self):
        self.name = self.name.upper()

    def show(self):
        print(self.name, self.loc, self.age)