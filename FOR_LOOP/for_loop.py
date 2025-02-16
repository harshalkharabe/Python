"""for loop
The  for  statement is used to iterate over the elements of a sequence (such
as a string, tuple or list) or other iterable object:
Syntax-1:
for variable in iterable:
    statement-1
    statement-2
for loop repeat statement-1,statement-2 based on length of iterable.
All collections are called iterable object."""

#HOW MANY TIMES PYTHON LOOP EXECUTE 
for ch in "ABC":
    print("Python")

# write a program to find length of string (count of characters)
str = input("Enter a string : ")
count = 0
for i in str:
    count+=1
print(f"Length of string is {count}")

# Write a program to count alphabets,digits and special characters in a given string
str = input("Enter any string :")
acount,dcount,scount=0,0,0
for i in str:
    if (i>='A' and i<='Z') or (i>='a' and i<='z'):
        acount+=1
    elif i>='0' and i<='9':
        dcount+=1
    else:
        scount+=1
print(f"In upper string there is {dcount} digits, {acount} alphabates & {scount} special character")

# Write a program to count vowels of input string
str = input("Enter a string :")
vcount = 0
for i in str:
    if i in "AEIOUaeiou":
        vcount+=1
print(f"Vowel count in upper string is {vcount}")

# Write a program to convert input string from lowercase to uppercas

str = input("Enter a string :")
str2 = ""
for ch in str:
    if (ch>='a' and ch<='z'):
        str2 = str2 + chr(ord(ch)-32)
    else:
        str2=str2+ch
print(f"Sring in upper case is {str2}")


for i in "Range":
    print(i,end='\t')