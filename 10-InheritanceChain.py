class Pet:
    def __init__(self,name):
        self.name = name

class Dog(Pet):
    def describe(self):
        return "the dog says: Woof!"

class LapDog(Dog):
    def describe(self):
        return "the lap dog says: Yip!"

class LoudLapDog(LapDog):
    def describe(self):
        return "the loud lap dog says: YIP!"

buck = Dog("Buck")
print(buck.describe())

shorty = LapDog("Shorty")
print(shorty.describe())

pip = LoudLapDog("Pip")
print(pip.describe())

print(isinstance(shorty,Pet))
print(isinstance(shorty,Dog))
print(isinstance(shorty,LapDog))
print(isinstance(shorty,LoudLapDog))