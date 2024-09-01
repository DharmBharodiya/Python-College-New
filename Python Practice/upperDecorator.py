def uppercaseDecorator(function):
    def wrapper():
        theString = function()#here the function() will return the string, which will be stored in the theString variable and the upper() would be applied to it
        make_uppercase = theString.upper()
        return make_uppercase
    return wrapper

@uppercaseDecorator
def sayHi():
    return "Hi There"

print(sayHi())