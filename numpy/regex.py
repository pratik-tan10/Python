import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

for line in hand:
    line = line.rstrip()
    if re.search('^From', line):
        print(line)
        
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)
        
for line in hand:
    line = line.rstrip()
    if re.search('From:.+@*', line):
        print(line)
        
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]', line)
    if len(x) > 0:
        print(x)

for line in hand:
    line = line.rstrip()
    x = re.search('^X\S*: ([0-9.]+)', line)
    if len(x)>0:
        print(x)

