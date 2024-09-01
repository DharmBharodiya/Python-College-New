#simple function
def children(fname, lname):
    print("First name: ", fname)
children("dharm","jain")

#arbitary arguments
def childrens(*kids):#in the case when you don't know how many arguments are going to be passed
    print("The kid in the middle is: ", kids[1])

childrens("dharm","kendall","justin")

#keywords arguments
def people(p1, p2, p3):
    print("The middle one is: ", p2)

people(p3="jlo", p1="dharm", p2="siya")

#arbitary arguments + keyword arguments
def person(**persons):
    print(persons["middle"],"is the most beautiful.")

person(first="dharm",middle="dani",last="john")

#default parameter value
def country(name="India"):
    print("Country: ", name)

country()
country("Uzbekistan")


#passing list as an argument
theList = [1,2,3,4,5]
def listIterator(newList):
    for x in newList:
        print(x, end=" | ")
listIterator(theList)

print()
#passing tuple as an argument
theTuple = (1,2,3,4,5)
listIterator(theTuple)
