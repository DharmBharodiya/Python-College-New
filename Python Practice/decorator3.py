# def theDecorator(func):
#     def wrapper(name, lastname):
#         print("decoratorrrrrrrrrr")
#         func(name, lastname)
#         print("decoratorrrrrrrrrr")
#     return wrapper

# def uppercaseDecorator(func):
#     def wrapper(name, lastname):
#         thefunc = func(name, lastname)
#         uppercased = thefunc.upper()
#         return uppercased
#     return wrapper

# @theDecorator
# def showDetails(name, lastname):
#     print(f"{name} {lastname}")

# @uppercaseDecorator
# @theDecorator
# def newfunc(name, lastname):
#     return f"{name} {lastname}"
# showDetails("dharm","bharodiya")
# print(newfunc("dharm","bharodiya"))

def theDecorator(func):
    def wrapper(name, lastname):
        print("decoratorrrrrrrrrr")
        func(name, lastname)
        print("decoratorrrrrrrrrr")
    return wrapper

def uppercaseDecorator(func):
    def wrapper(name, lastname):
        # Call the decorated function and ensure it returns a string
        result = func(name, lastname)
        uppercased = result.upper()
        return uppercased
    return wrapper

@theDecorator
def showDetails(name, lastname):
    print(f"{name} {lastname}")

@uppercaseDecorator
@theDecorator
def newfunc(name, lastname):
    return f"{name} {lastname}"

# Usage
showDetails("dharm", "bharodiya")
print(newfunc("dharm", "bharodiya"))
