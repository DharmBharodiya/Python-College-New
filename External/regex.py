import re

# pattern = r"[A-Za-z^\s]"
pattern = r"^.*[0-9]$"
testString = "thi2 i2 a 2tring that is to be t3st3d 3454"

match = re.match(pattern,testString)
if match:
    print("WOOOOHOOOOOO MOTHERFUKERRRRRR")
else:
    print("Fuck off")