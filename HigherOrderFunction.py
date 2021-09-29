def applyToEachString(stringFunction, stringList):
    myList = []
    for item in stringList:
        myList.append(stringFunction(item))
    return myList
 
allUpperCase = applyToEachString(str.upper, ['Building', 'ROAD', 'tree'] )
print(allUpperCase)
