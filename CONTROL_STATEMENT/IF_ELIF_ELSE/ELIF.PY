"""If..elif..else (if..else ladder)
This syntax is used for checking more than one condition.
In this syntax there is another keyword used elif.
Syntax:
if codnition1:
    statement-1
elif condition2:
    statement-2
elif condition3:
    statement-3
…
else:
    statement-4
statement-5
if condition1 is True, Python execute
statement-1,statement-5
if condition is False, condition2 is
True, Python execute statement-2
and statement-5
if condition1,condition2 are False and
condition3 is True, Python executes
statement-3,statement-5
if condition1,condition2, condition3
are false, python execute statement-4
and statement-5"""

# Write a program to find input number is +ve,-ve or zero
num = int(input("Enter number : "))
if num>0:
    print("+ve")
elif(num<0):
    print("-ve")
else:
    print("Zero")

# Write a program to find input character is alphabet, digit or special character
ch = input("Enter a character : ")
if (ch>="A" and ch>="Z") or (ch>='a' and ch<='z'):
    print("it is character")
elif ch>='0' and ch<='9':
    print("it is a digit")
else:
    print("it is special character")

# Write a program to find max of 3 numbers

x = int(input("enter a number : "))
y = int(input("enter a number : "))
z = int(input("enter a number : "))

if x==y and x==z:
    print("Equal")
if x>=y and x>=z:
    print(f"{x} is greater")
elif y>=z:
    print(f"{y} is greater")
else:
    print(f"{z} is greater")
