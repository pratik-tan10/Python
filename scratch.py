Str1= "food"
Str2 = "dorm"
count1,count2 = 0,0
for letter in Str1:
	if letter in Str2:
		count1+=1
for letter in Str2:
	if letter in Str1:
		count2+=1
Count = count1+count2
print(f"{Str1}:{count1},{Str2}:{count2},Total = {Count}")
