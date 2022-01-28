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
      
#Eval function dynamically changes the variable to appropriate number type
num1 = eval(input("Input a number."))
      
def anagram(x,y):
    def dix(st):
        d = {}
        s = st.lower()
        for each in s:
            if each in d: d[each]+=1
            else: d[each]=1
        return d
    
    if dix(x)==dix(y):print("YES")
    else: print("NO")

anagram('hi?','?ih')

def vc(s):
    v = 'aeiou'
    c = 0
    sl = s.lower()
    i = 0
    for each in sl:
        if each in v:
            c+=1
            print(i)
        i+=1
            
    print(f'vowel count = {c}')

vc('monseur malla')
#urlify
x = ['h', 'i', ' ', 'b', 'u', 'd', ' ', ' ']
y=[]
c = 0
for a in x:
    if a !=" ":
        y.append(a)
    else:
        y.extend(['%','2','0'])
    c+=1
    if c==6:break
print(x,y)

#string compression
x = 'aaaaaabbbbbbbchdeen'
def stc(x):
    cs = []
    f = x[0]
    i = 1
    for c in x[1:]:
        if c == f:
            i+=1
        else:
            cs.extend([f,str(i)])
            f = c
            i=1
    cs.extend([c,str(i)])
    css = "".join(cs)
    return css if len(css)<len(x) else x
print(stc('aaaabbccd'))
            
        
