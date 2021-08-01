class Dog:

    

    species = 'mammal'
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#
#
jin = Bulldog("Jin", 12)
print(jin.description())

#
#
print(jin.run("slowly"))

#
print(isinstance(jin, Dog))

#
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

#
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

#
print(isinstance(julie, Bulldog))