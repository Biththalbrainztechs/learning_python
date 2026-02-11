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