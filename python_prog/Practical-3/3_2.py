x = str(input("Enter the string:")) 
upper = 0 
lower = 0  
digits = 0 
letter = 0
space = 0 
special = 0 
for a in x: 
    if a.isupper(): 
        upper += 1 
        letter += 1 
    elif a.islower(): 
        lower += 1 
        letter += 1 
    elif a.isalnum(): 
        digits += 1 
    elif a.isspace(): 
        space += 1 
    elif not a.isalnum(): 
        special += 1 
print(digits,letter,upper,lower,space,special) 