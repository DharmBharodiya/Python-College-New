sentence = input("enter a string: ")

num_digits = 0
num_letter = 0
num_lowercase = 0
num_uppercase = 0
num_spaces = 0

def countChars(sentence):
    global num_digits, num_letter, num_lowercase, num_uppercase, num_spaces
    for char in sentence:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letter += 1
            if char.isupper():
                num_uppercase += 1
            else:
                num_lowercase += 1
        elif char.isspace():
            num_spaces += 1

#calling the function for the user input 'sentence'

countChars(sentence)

print("Number of digits: ", num_digits)
print("Number of letters: ", num_letter)
print("Number of uppercase letters: ", num_uppercase)
print("Number of lowercase letters: ", num_lowercase)
print("Number of spaces: ", num_spaces)