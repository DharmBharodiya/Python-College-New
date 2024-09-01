def newDecorator(func):
    def kushal(name, lastname):
        print("The details of the person is: ")
        func(name, lastname)
        print("Thank you for visiting.")
    return kushal

@newDecorator
def patientDetails(name, lastname):
    print(f"Name: {name} {lastname}")

@newDecorator
def employeeDetails(name, position):
    print(f"Name: {name} Position: {position}")

patientDetails("Dharm","Bharodiya")
employeeDetails("Ramu","Karigar")
