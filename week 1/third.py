class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog object
dog1 = Dog("Philo", 5)
dog2 = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} is {}."
.format(dog1.name, dog1.age, dog2.name, dog2.age))

# Is Philo a mammal?
if dog1.species == "mammal":
    print("{} is a {}!".format(dog1.name, dog1.species))