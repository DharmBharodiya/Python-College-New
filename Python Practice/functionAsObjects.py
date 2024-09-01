# functions are the first class objects which means that it can pe passed as an argument of other functions
# it can be assigned to a variable, it can pe returned from a function
# it is an instance of object type
# you can store functions in data structures such as hash tables,lists, etc....

def shout(text):
    return text.upper()
print(shout("hello"))
yell = shout
print(yell("helllooooo"))

#passing function as argument
def shoutAgain(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func('''hi, i am created by function passed as an argument''')
    print(greeting)

greet(shoutAgain)
greet(whisper)

#returning functions from other functions
def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_15 = create_adder(15)
print(add_15(10))