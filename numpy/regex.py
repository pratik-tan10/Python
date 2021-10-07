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
        
