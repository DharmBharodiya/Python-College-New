import re

pattern = r"ab+"

# testStrings = ["ab","aabbb","acbbbb","anbbb","aaabbbnn"]



#question 2, sequence of lowercase letters joined with underscore
# pattern = r"^[a-z]+_[a-z]+$"
# testStrings = ["ab_cd", "efgh_ijkl", "abb+", "_b", "b_"]

#question 3, match all the five character long words
# pattern = "^[a-zA-Z]{5}$"
# testStrings = ["dharm","crazy", "elephant", "samay", "kaludada"]

#question 4, match the email id
# pattern = "^([\w\d\.-_]+)@([\w\d]+)\.(com|edu|org)$"
topLevelPattern = r"@[\w.-]+\.(\w+)$"
testStrings = ["dharm@gmail.com","kfu$cks@yatri.com","rak_shit@yahoo.org","dhaval@diyako.nahidiya"]

match = re.search(topLevelPattern, testStrings[0])
if match:
    print(match.group(1))
else:
    print("Fuck off")

# for test in testStrings:
#     if re.search(pattern, test):
#         print(f"'{test}' matches the pattern.")
#     else:
#         print(f"'{test}' does not match the pattern.")