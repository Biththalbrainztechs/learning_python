class Dog:
    """A simple class representing a dog"""
    pass  # Empty class for now

# Create an object (instance) of the Dog class
my_dog = Dog()
print(f"I created a dog: {my_dog}")
print(f"Type: {type(my_dog)}")
print()
# You can create multiple objects from the same class
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()

# print(f"Dog 1: {dog1}")
# print(f"Dog 2: {dog2}")
# print(f"Dog 3: {dog3}")
# print(f"Are they the same? {dog1 is dog2}")  # False - different objects!
# print()

class DogWithAttributes:
    """ A dog with attributes"""
    def __init__(self,name,breed,age):
        """ This is the Constructorr- it runs when you create a new dog.
       
         'self' refers to the specific object being created . 
        
        """

        self.name = name
        self.breed =breed
        self.age = age
        print(f"A new dog name {name} was created")

buddy = DogWithAttributes("Buddy","Golden Retriver",3)
max_boy = DogWithAttributes("Max","Beagal",5)
bella = DogWithAttributes("Bella","Labrador",2)

print()
print(f'{buddy.name} is {buddy.age} years old and {buddy.breed}')
print(f'{max_boy.name} is {max_boy.age} years old and {max_boy.breed}')
print(f'{bella.name} is {bella.age} years old and {bella.breed}')
print()

"""
'self' is a reference to the current instance.
When you call: buddy.name
Python translates it to: DogWithAttributes.name(buddy)

That's why methods need 'self' as the first parameter!
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):

        "Method that uses self to access this person's attributes"

        print(f'Hi I am {self.name} and i am {self.age} years old')


alice = Person("Alice",25)
bob = Person("BOb",30)

alice.introduce()
bob.introduce()
print()

class Car:
    def __init__(self,brand,model,year=2045,color="black"):
        """
        Docstring for __init__
      Some parameters can have default values,
      If not provided, the default value is used
       """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def description(self):
        return f"{self.year} {self.brand} {self.model} {self.color}" 


car1=Car("Toyota","Camry")
car2= Car("Honda","Civic",2023)
car3 = Car("Ford","Mustang",2022,"Red")

print(car1.description())
print(car2.description())
print(car3.description())

class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
    
    def show(self):
        print(f"Count: {self.count}")


counter1 = Counter(0)
counter2 = Counter(100)

print("Counter 1:")
counter1.show()
counter1.increment()
counter1.increment()
counter1.show()

print("\nCounter 2:")
counter2.show()
counter2.increment()
counter2.show()


print("=" * 60)
print("KEY CONCEPTS TO REMEMBER:")
print("=" * 60)
print("1. Class = Blueprint (like a cookie cutter)")
print("2. Object = Instance (like an actual cookie)")
print("3. __init__ = Constructor (runs when object is created)")
print("4. self = Reference to the current instance")
print("5. Attributes = Data stored in each object")
print("6. Each object is independent from others")
print("=" * 60)