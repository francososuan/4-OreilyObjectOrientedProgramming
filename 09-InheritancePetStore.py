# repetitive

class Dog_1:
    def __init__(self,name):
        self.name = name
    def describe(self):
        return "the dog says: Woofs!"

class Bird_1:
    def __init__(self,name):
        self.name = name
    def describe(self):
        return "the dog says: Chirp!"

class Cat_1:
    def __init__(self,name):
        self.name = name
    def describe(self):
        return "the dog says: Meow!"

fido = Dog_1("Fido")
print(fido.describe())


class Pet:
    def __init__(self,name):
        self.name = name

class Dog(Pet):
    def describe(self):
        return "The dog says: Woof!"

class Cat(Pet):
    def describe(self):
        return "The cat says: Meow!"

jiro = Dog("Jiro")
print(jiro.describe())

archer = Cat("Archer")
print(archer.describe())