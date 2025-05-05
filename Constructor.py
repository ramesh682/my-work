
class Person:
    def __init__(self, name, age):
        
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Ramesh", 25)
person2 = Person("Sita", 30)


person1.introduce()
person2.introduce()
