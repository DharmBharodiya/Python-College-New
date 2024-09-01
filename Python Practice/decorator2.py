def theSecondDecorator(function):
    def wrapper():
        print("start of the decorator")
        function()
        print("end of the decorator")
    return wrapper # returning the wrapper is of utmost importance, otherwise the decorator won't work and mainly the function too will not work

@theSecondDecorator
def thePrinter():
    for x in range(12):
        print(x)

thePrinter()