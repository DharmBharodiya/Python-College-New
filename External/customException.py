class NewError(Exception):
    pass

try:
    a = int(input("Enter a new number"))
    if a < 0:
        raise NewError
except NewError:
    print("The number is just too small.")
finally:
    print("Code reaches its end.")