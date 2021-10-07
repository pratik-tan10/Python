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

