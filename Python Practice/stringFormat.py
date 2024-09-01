name = "Dharm"
age = 14

print("Using + operator")
print("My name is " + name + " and age is " + str(age))
# print("My name is " + name + " and age is " + age)#this will create an error because only strings can be concatenated and not the integers

print("Using '%' operator")
print("My name is %s and age is %d." % (name, age))

print("Using format method")
print("My name is {} and age is {}.".format(name,age))
print("Hello world. I am {} and I am {} years old.".format(name, age))

print("using f-strings")
print(f"My name is {name} and age is {age}.")
print(F"Hello world. I am {name} and I am {age} years old.")

print("Using named indices")
theString = "My name is {username} and age is {userage}."
print(theString.format(username=name,userage=age))

theNewString = "Hello World. I am {name} and I am {age} years old"
print(theNewString.format(name='dharm', age='14'))


numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))