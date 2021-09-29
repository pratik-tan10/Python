def applyToEachString(stringFunction, stringList):
    myList = []
    for item in stringList:
        myList.append(stringFunction(item))
    return myList
 
allUpperCase = applyToEachString(str.upper, ['Building', 'ROAD', 'tree'] )
print(allUpperCase)
allLowerCase = applyToEachString(str.lower, ['Building', 'ROAD', 'tree'] )
print(allLowerCase)
print([ s.upper() for s in ['Building', 'ROAD', 'tree'] ])
