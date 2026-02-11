"""
DAY 1 - MODULE 1: Classes and Objects
======================================

What you'll learn:
- What is a class?
- What is an object?
- Creating classes
- Creating instances (objects)
- Instance attributes
- The __init__ method
"""

# ============================================================
# PART 1: WHAT IS A CLASS?
# ============================================================

"""
A class is a BLUEPRINT for creating objects.
Think of it like a cookie cutter - the class is the cutter,
the objects are the cookies you make with it.

Example analogy:
- Class = "Dog" (the concept of a dog)
- Objects = Your actual dogs: Buddy, Max, Bella
"""

# ============================================================
# PART 2: YOUR FIRST CLASS
# ============================================================

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

print(f"Dog 1: {dog1}")
print(f"Dog 2: {dog2}")
print(f"Dog 3: {dog3}")
print(f"Are they the same? {dog1 is dog2}")  # False - different objects!
print()

# ============================================================
# PART 3: ADDING ATTRIBUTES
# ============================================================

class DogWithAttributes:
    """A dog with attributes"""
    
    def __init__(self, name, breed, age):
        """
        This is the CONSTRUCTOR - it runs when you create a new dog.
        
        'self' refers to the specific object being created.
        Think of 'self' as "this particular dog"
        """
        self.name = name      # This dog's name
        self.breed = breed    # This dog's breed
        self.age = age        # This dog's age
        print(f"🐕 A new dog named {name} was created!")

# Create dogs with different attributes
buddy = DogWithAttributes("Buddy", "Golden Retriever", 3)
max_dog = DogWithAttributes("Max", "Beagle", 5)
bella = DogWithAttributes("Bella", "Labrador", 2)

print()
print(f"{buddy.name} is a {buddy.age}-year-old {buddy.breed}")
print(f"{max_dog.name} is a {max_dog.age}-year-old {max_dog.breed}")
print(f"{bella.name} is a {bella.age}-year-old {bella.breed}")
print()

# ============================================================
# PART 4: UNDERSTANDING 'self'
# ============================================================

"""
'self' is a reference to the current instance.
When you call: buddy.name
Python translates it to: DogWithAttributes.name(buddy)

That's why methods need 'self' as the first parameter!
"""

class Person:
    def __init__(self, name, age):
        self.name = name  # self.name = the name of THIS person
        self.age = age    # self.age = the age of THIS person
    
    def introduce(self):
        """Method that uses self to access this person's attributes"""
        print(f"Hi! I'm {self.name} and I'm {self.age} years old.")
        # 'self.name' means "this person's name"
        # 'self.age' means "this person's age"

alice = Person("Alice", 25)
bob = Person("Bob", 30)

alice.introduce()  # Uses Alice's attributes
bob.introduce()    # Uses Bob's attributes
print()

# ============================================================
# PART 5: DEFAULT VALUES
# ============================================================

class Car:
    def __init__(self, brand, model, year=2024, color="Black"):
        """
        Some parameters can have default values.
        If not provided, the default is used.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def description(self):
        return f"{self.year} {self.color} {self.brand} {self.model}"

# Create cars with and without all parameters
car1 = Car("Toyota", "Camry")                    # Uses defaults
car2 = Car("Honda", "Civic", 2023)               # Override year
car3 = Car("Ford", "Mustang", 2022, "Red")       # Override both

print(car1.description())
print(car2.description())
print(car3.description())
print()

# ============================================================
# PART 6: MODIFYING ATTRIBUTES
# ============================================================

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance:.2f}")

# Create account
account = BankAccount("Alice", 1000)
account.show_balance()

# Modify attributes directly (not recommended, but possible)
account.balance = 1500
account.show_balance()

# Better: use methods to modify (we'll learn this in Module 2)
print()

# ============================================================
# PART 7: MULTIPLE INSTANCES ARE INDEPENDENT
# ============================================================

class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
    
    def show(self):
        print(f"Count: {self.count}")

# Create two separate counters
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

# They're independent - changing one doesn't affect the other!
print()

# ============================================================
# KEY TAKEAWAYS
# ============================================================

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