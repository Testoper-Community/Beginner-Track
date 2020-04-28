# Variables Declaration
strCommunityName = "Testoper"
bStr = '10'
cNum = 10
dFlt = 5.3
CNUM = 20

# Re-Declaration
bStr = 33
cNum = "Lab1"

# Concatenate
strHello = "Hello"
strName = "Hetal Patel"
greetingStr = strHello + strName + "....!"

# Delete
del cNum
# below line will create an error because aStr is deleted
# print(cNum)

# String
varStr = 'This is a string variable'
print(varStr)
varSTR = "This is also a string variable but different that above"
print(varSTR)

# String format option, String formatter
varLabNum = 1
varTrackName = "Python"
print("This a lab number %s for beginner track of learning %s" % (varLabNum, varTrackName))
print("This a lab number {0} for beginner track of learning {1}".format(varLabNum, varTrackName))
print(f"This a lab number [{varLabNum}] for beginner track of learning {varTrackName}")
print("This a lab number {num} for beginner track of learning {track}".format(num=1, track="Python"))