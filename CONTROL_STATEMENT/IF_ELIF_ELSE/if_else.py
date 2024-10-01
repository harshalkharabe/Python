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

age = int(input("Enter age :"))
if age>=18:
    print("Adult")
else:
    print("Child")

number = int(input("Enter number : "))
if number%5==0:
    print(f"{number} is devisible by 5")
else:
    print(f"{number} not divisible by 5")