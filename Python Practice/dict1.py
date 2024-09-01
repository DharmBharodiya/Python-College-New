d =  dict([
    ("dharm","bharodiya"),
    ("diya","jain"),
    ("hani","patel")
])

print(d)


d1 = dict(
    dharm="bharodiya",
    diya="jain",
    vishwa="gandhi"
)

print(d1)

Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict["dharm"] = "bharodiya"
Dict["diya"] = "jain"
Dict["sachi"] = "patel"

print(Dict)

Dict1 = {}
Dict1['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict1)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

car["secondColor"] = "red"
print(car)

car.pop("color")
print(car)

car.popitem()
print(car)

del car["model"]
print(car)

newdict = {"brand": "Ford",
  "model": "Mustang",
  "year": 1964}
newdict.clear()
print("Cleared Dict. : ", newdict)


keyList = ["this","they","them"]
valueList = ["noun","adjective","pronoun"]
fromKeysDict = dict.fromkeys(keyList,valueList)
print(fromKeysDict)


theDays = ["Sunday","Monday","Tuesday","Wednesday"]
print(theDays[-3:-1])

myStr = "CVMU is the best University"
print(myStr[15::1])
print(myStr[-10:-1:2])