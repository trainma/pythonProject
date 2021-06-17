# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Dog:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting")

    def rollover(self):
        print(f"{self.name} rolled over")

my_dog=Dog('jack',6)
print(f"My dog is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.rollover()