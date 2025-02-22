# steps:
#1)
# You must create at least TWO classes.
# For now, just focus on:
# Planning Your Two Classes
# Creating a Basic Constructor (__init__() method)

#2)
# Each of those classes must have at least THREE attributes and THREE methods.
# You may need to create some instances of your classes to test your methods.

#3)
# Your classes should be able to describe themselves (through a __repr__() method).
# You will need to create at least one instance of your classes to test your __repr__() method.

#4)
# If you haven’t already, create at least TWO instances of every one of your classes.
# Test all of the methods you created on both of the objects you create.

#5)
# Create some methods, or additional attributes, that make your two Classes able to interact with each other.


#TERMINAL GAME: GHOSTS AND VILLAINS

class Ghost:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.anger = self.age * 2
        self.transparency = self.anger * 2
    def __repr__(self):
        return f"My name is {self.name}, i have {self.age} years old."
    
class Villain:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.fear = self.age / 2
    def __repr__(self):
        return f"My name is {self.name}, I am {self.age} years old and my fear level is {self.fear}"



ghost1 = Ghost("Arthur", "500")
villain1 = Villain("Marcus", 23)
print(ghost1)
print(villain1)
