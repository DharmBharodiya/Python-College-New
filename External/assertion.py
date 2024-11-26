try:
    a = int(input("Enter a number"))
    assert a > 0, "The number should be greater than zero."
except AssertionError:
    print("The number is less than zero.")
    print()