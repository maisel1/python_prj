class Dog:
  def __init__(self, input_name, input_breed, input_age = 0, input_friendliness=True):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_friendly = input_friendliness
    self.friends = []

  def __repr__(self):
    # Printing a Dog will tell you its name, its breed, its age, if it's friendly, and how many friends it has.
    description = f"This {self.breed} named {self.name} is {self.age} years old and has {self.friends} friends."
    if self.is_friendly:
      description += " {name} is a friendly dog.".format(name = self.name)
    else:
      description += " {name} is an unfriendly dog.".format(name = self.name)
    return description

new_dog = Dog("Toby", "Maltese")
print(new_dog)