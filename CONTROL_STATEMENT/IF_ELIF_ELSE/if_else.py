"""If..else
This syntax is having two blocks
1. if block
2. else block

Syntax:
if condition:
    Statement-1
    Statement-2
else:   
    statement-3
    statement-4

statement-5
if condition is True, python
execute statement-1,statement-
2 and statement-5
if condition is False, python
execute statement-3,statement-
4 and statement-5"""

name = input("Enter name :")
if name == "Harshal":
    print("Oo you guess my name ")
else:
    print("Oops wrong name")

#WAP TO CHECK A PERSON IS ADULT OR CHILD
age = int(input("Enter age :"))
if age>=18:
    print("Adult")
else:
    print("Child")

#WAP TO CHECK NUMBER IS DIVISIBLE BY 5 OR NOT 
number = int(input("Enter number : "))
if number%5==0:
    print(f"{number} is devisible by 5")
else:
    print(f"{number} not divisible by 5")

#WAP TO CHECK NUMBER IS THERR DIGIT OR NOT
num = int(input("Enter number :"))
if num>=100 and num<=999:
    print(f"{num} is three digit number")
else:
    print(f"{num} is not three digit number")