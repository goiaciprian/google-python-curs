

class Animal(object):
  def __init__(self, age) -> None:
      self.age = age
      self.name = None

  def get_age(self):
    return self.age

  def get_name(self):
    return self.name

  def set_age(self, newage):
    self.age = newage

  def set_name(self, newname=""):
    self.name = newname

  def __str__(self):
    return f"animal: nume {str(self.get_name())}, varsta {str(self.get_age())}"


class Cat(Animal):

  def __str__(self):
    return f"cat: nume {str(self.get_name())}, varsta {str(self.get_age())}"

  def speak(self):
    print("meow")

class Person(Animal):
  def __init__(self, name: str, age: int):
    Animal.__init__(self, age)
    self.set_name(name)
    self.friends = []
  
  def __str__(self):
      return f"person {str(self.get_name())}, varsta {str(self.get_age())}"

  def get_friends(self):
    return self.friends

  def set_friends(self, friends: list):
    self.friends = friends

  def add_friend(self, friend_name):
    if friend_name not in self.get_friends():
      self.friends.append(friend_name)

animal1 = Animal(4)
animal1.set_name("Scooby Doo")
animal1.set_age(5)


print(animal1)
print(animal1.get_name())
print(animal1.get_age())

mimi = Cat(10);
print(mimi)
mimi.speak()

john = Person("John", 25)
print(john)
john.add_friend('Ionut')
john.add_friend('Ionut')
john.add_friend('George')
print(john.get_friends())