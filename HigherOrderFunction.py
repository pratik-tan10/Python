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
