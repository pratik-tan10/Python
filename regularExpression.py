import re
personList = [ 'Julia Smith', 'Francis Drake', 'Michael Mason',  
                'Jennifer Johnson', 'John Williams', 'Susanne Walker',  
                'Kermit the Frog', 'Dr. Melissa Franklin', 'Papa John', 
                'Walter John Miller', 'Frank Michael Robertson', 'Richard Robertson', 
                'Erik D. White', 'Vincent van Gogh', 'Dr. Dr. Matthew Malone', 
                'Rebecca Clark' ]
pattern = ".u"

compiledRE = re.compile(pattern)

for person in personList:
  if compiledRE.match(pattern, person):
    print(person)
