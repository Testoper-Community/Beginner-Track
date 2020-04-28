# Spanning a string and use of single and double quotes
varSpanStr = """This is line one
This is line two
This is line three"""
print(varSpanStr)
print("*" * 5)

# Exercise: try to write 3 lines of message where you draw stars in points for knowledge of the Python you have,
# after fibishing exercise please clean up your variables
# get name and point from user : hint use int(points) for number of starts
# For example "My name is Hetal Patel, I have The Python level of 4 points [****],
# I am learning an advance Python"

# get part of a string

varLongStr = "This is a Testoper community and today we are learning the Python"
strLength = len(varLongStr)
print(strLength);
varCharPositionofStr = varLongStr[8]
print(varCharPositionofStr)
varPartOfStr = varLongStr[10:28]
print(varPartOfStr)
# negative index -1, -2 etc
# [2:-2] ignore first two and last two characters

# Exercise : Find string 'We are learning the Python'

# String functions upper, lower
strLength = len(varLongStr)
strUpper = varLongStr.upper()
strLower = varLongStr.lower()
intIndex = varLongStr.find('T')
# case sensitive
intNagIndex = varLongStr.find('A')
intStartingIndex = varLongStr.find('Python')

# Replace

strReplaced = varLongStr.replace('Python', 'Java')
# try to find 'java' and see what is your out put
# replace back 'Java' with 'Python'

# check substring
isSubstring = 'Python' in varLongStr
print(isSubstring)