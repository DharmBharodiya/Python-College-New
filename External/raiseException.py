try:
    thenum = int(input("Enter a number"))
    if thenum < 0:
        raise ValueError("The number entered is not greater than zero.")
except ValueError as ve:
    print(ve)
finally:
    print("The code reached its end.")