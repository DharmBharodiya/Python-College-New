class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute

    # Getter for name
    @property
    def name(self):
        return f"Hello, {self._name}"

    # Setter for name
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name cannot be empty")

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be positive")

# Example usage
person = Person("Alice", 30)

print(person.name)  # Calls the getter for name
print(person.age)   # Calls the getter for age

# Set new values
person.name = "Bob"
person.age = 35

print(person.name)  # Calls the getter for name
print(person.age)   # Calls the getter for age

# Attempt to set invalid values
try:
    person.name = ""   # This will raise a ValueError
except ValueError as e:
    print(e)

try:
    person.age = -5    # This will raise a ValueError
except ValueError as e:
    print(e)
