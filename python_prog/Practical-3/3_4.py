def DecimalToBinary(n) : 
    i = 0 
    Binary = 0 
    while(n > 0) : 
        rem = n % 2 
        Binary += (rem*pow(10,i)) 
        n //= 2 
        i += 1 
    return Binary 
 
def DecimalToOctal(n) : 
    i = 0 
    Octal = 0 
    while(n > 0) : 
        rem = n % 8 
        Octal += (rem*pow(10,i)) 
        n //= 8 
        i += 1 
    return Octal 
 
def DecimalToHexadecimal(n) : 
    Hexadecimal_range = "0123456789ABCD" 
    Hexa_Decimal = "" 
    if n == 0 : 
        return 0 
    while(n > 0) : 
        rem = n % 16 
        Hexa_Decimal = Hexadecimal_range[rem] + Hexa_Decimal 
        n //= 16 
    return Hexa_Decimal 
 
Num = int(input("Enter a number : ")) 
print("Decimal = ", Num) 
print("Binary = ", DecimalToBinary(Num)) 
print("Octal = ", DecimalToOctal(Num)) 
print("Hexadecimal = ", DecimalToHexadecimal(Num))