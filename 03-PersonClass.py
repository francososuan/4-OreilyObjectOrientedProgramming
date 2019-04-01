class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first + " " + self.last

    def formal_name(self,title):
        return title + " " + self.full_name()


person = Person("John","Smith")
print(person.first)
print(person.last)

person_you = Person("Franco", "Sosuan")
print(person_you.formal_name("Dr."))