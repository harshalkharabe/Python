#Remove duplicates in string
s1 = input("Enter string : ")
s2 = ''

for i in s1:
    if i not in s2:
        s2 += i
print(f"After Removing Duplicates : {s2}")

#PYTHON PROGRAM TO GIVE LEAST FREQUENCY (COUNT) OF CHARACTER
s1 = "python programming"
s2 = ''
for i in s1:
    if i not in s2:
        s2 += i
mcount = s1.count(s1[0])
print(s2)
ch = s1[0]
for i in s2:
    c = s1.count(i)
    if mcount>c:
        mcount=c
        ch = i
        print(True)
print(ch,"-->",mcount)