#Python 2
print("Hello world")
print "Hello world"

#Python 3
print("Hello world")

name = input("Enter your name")

#with string concatenation
print("Hello " +name+" ". Nice to meet you!")

#with string format
print("Hello {} . Nice to meet you!".format(name))
 
number = int(input("Please enter a whole number."))
      
#python ternary ...if...else....

print("That's a large number" if number>100 else "That's a small number")
      
l = list(range(1,20))

#iterate through a list using for loop
for i in l: print(i)

#iterate through a list using while loop
j = 0
while(j<len(l)):
      print l[j]
      j+=1

#while loop with break
k = 0
while True:
      print(l[k])
      if k>=len(l): break

#Creating list using lambda
v = list(map(lambda x: x+1, l))
      
#Creating list using short hand
w = [k+1 for k in l]

def subt(x): return ("Odd",x) if x%2==1 else ("Even",x)
      
q = list(map(subt,l))
      
