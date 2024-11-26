def minimum(m,n) : 
    if m < n : 
        return m 
    else : 
        return n 
def FindHCF(m,n) : 
    min = minimum(m,n) 
    for i in range(1, min+1) : 
        if m%i==0 and n%i==0 : 
            hcf = i 
        else : 
            hcf = 1 
    return hcf 
num1 = int(input("enter number 1 : ")) 
num2 = int(input("enter number 2 : ")) 
HCF = FindHCF(num1, num2) 
print("The HCF/GCD of ",num1," and ",num2," is = ",HCF,".")