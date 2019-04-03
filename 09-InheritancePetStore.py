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

print("")
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

print(jiro.name + " " + jiro.describe())
print(archer.name + " " + archer.describe())

# Challenge: placing describe() into the Pet Class
print("")


class Pet_2:
    sound = ""
    def __init__(self,name):
        self.name = name
    def describe(self):
        return print("the {} says: {}!" .format(self.__class__.__name__.lower(),self.sound))

class Dog_2(Pet_2):
    sound = "Woof"

class Cat_2(Pet_2):
    sound = "Meow"

class Bird_2(Pet_2):
    sound = "Chirp"

mica = Dog_2("Mica")
nyan = Cat_2("Nyan")
tweety = Bird_2("Tweety")

mica.describe()
nyan.describe()
tweety.describe()
