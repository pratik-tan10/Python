import re 
 
personList = [ 'Julia Smith', 'Francis Drake', 'Michael Mason',  
                'Jennifer Johnson', 'John Williams', 'Susanne Walker',  
                'Kermit the Frog', 'Dr. Melissa Franklin', 'Papa John', 
                'Walter John Miller', 'Frank Michael Robertson', 'Richard Robertson', 
                'Erik D. White', 'Vincent van Gogh', 'Dr. Dr. Matthew Malone', 
                'Rebecca Clark' ] 
 
pattern = "John"
compiledRE = re.compile(pattern) 
 
for person in personList: 
     match = compiledRE.match(person) 
     if match: 
         print(match.group()) 
         print(match.start()) 
         print(match.end()) 
         print(match.span()) 
