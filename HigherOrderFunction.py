def applyToEachString(stringFunction, stringList):
    myList = []
    for item in stringList:
        myList.append(stringFunction(item))
    return myList
 
allUpperCase = applyToEachString(str.upper, ['Building', 'ROAD', 'tree'] )
print(allUpperCase)
allLowerCase = applyToEachString(str.lower, ['Building', 'ROAD', 'tree'] )
print(allLowerCase)
print( [(lambda s: s[:1].upper() + s[1:].lower())(s) for s in ['Building', 'ROAD', 'tree'] ])

def capitalizeFirstCharacter(s):
    return s[:1].upper() + s[1:].lower()
 
allCapitalized = applyToEachString(capitalizeFirstCharacter, ['Building', 'ROAD', 'tree'] )
print(allCapitalized)

allCapitalized = applyToEachString(lambda s: s[:1].upper() +  s[1:].lower(), ['Building', 'ROAD', 'tree'] )
print(allCapitalized)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def applyToEachNumber(numberFunction, numberList):
    l = []
    for item in numberList:
        l.append(numberFunction(item))
    return l
 
roundedNumbers = applyToEachNumber(round, [12.3, 42.8] )
print(roundedNumbers)
#==========================================================================================
#Map

map(str.upper, ['Building', 'Road', 'Tree'])
 
map(lambda s: s[:1].upper() + s[1:].lower(), ['Building', 'ROAD', 'tree']) # uses lambda expression for only first character as upper-case
 
map(round, [12.3, 42.8])


import operator
map(operator.add, [1,3,4], [4,5,6])

#==================================================================================
newList = list(filter(lambda s: s.startswith('R'), ['Building', 'ROAD', 'tree']))
print(newList)
