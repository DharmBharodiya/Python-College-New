def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b) 

# Example usage
num1 = 60
num2 = 48
print(f"GCD of {num1} and {num2} is: {gcd_recursive(num1, num2)}")
