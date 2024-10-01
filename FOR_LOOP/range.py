"""range datatype
range is a sequence data type.
range is an immutable sequence data type.
range data type is used for generating sequence of integer values.
The range type represents an immutable sequence of numbers and is
commonly used for looping a specific number of times in for loops.

range is an iterable or collection.
Syntax-1: range(stop)
Syntax-2: range(start,stop,step=1)"""

"""Range object is created with 3 attributes or values.
1. Start
2. Stop
3. Step
range data type is used for generating integer value in increment order or
decrement order.
Start : represents starting value of range (included)
Stop : represents ending value of range (excluded)
Step : difference between values within range (increment or decrement)
Syntax-1: range(stop)
Default start=0,step=1
This syntax always generate +ve range in ascending order"""

r = range(1,11)
print(r)

for i in r:
    print(i)

for i in range(5,-5,-1):
    print(i)

for i in range(100,-100,-23):
    print(i)

for i in range(-50,-5,5):
    print(i)

# Write a program to generate ASCII Table for Uppercase Alphabes
for i in range(65,91):
    print(f"{i} --> {chr(i)}")
for i in range(97,123):
    print(f"{i} --> {chr(i)}")

# Write a program to input 5 numbers and display
# total and avg
total = 0
for i in range(0,5):
    num = int(input("Enter a number : "))
    total = total+num
print(f"Total of 5 number is {total} and Average is {total/5}")

# Write a program to generate sum of sqr all the numbers
# from 1 to n

num = int(input("Enter a number :"))
for i in range(1,num+1):
    squr = i*i
    print(f"Square of {i} is {squr}")


# Write a program to generate math table of input number

num = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{num}x{i} == {num*i}")

# Write a progarm to find factorial of input number
number = int(input("Enter a number :"))
fact = 1
for i in range(1,number+1):
    fact *=i
print(f"Factorial of {number} is {fact}")

# Write a program to find input number is prime or not
number = int(input("Enter a num : "))
c = 0
for i in range(2,number):
    if number%i==0:
        c += 1
if c == 0:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
