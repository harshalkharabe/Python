# """While loop
# “while” keyword represents while loop
# While loop execute block of statements until given condition.
# Syntax:
# while condition:
#     statement-1
#     statement-2
# statement-3
# statement-1,statement-2 are executed until given condition is True, if
# condition is False, stop execution of while and continue with statement-3
# while loop required 3 statements
# 1. Initialization statement
# 2. Condition
# 3. Update statement
# Initialization statement defines initial value of condition
# Condition is a Boolean expression which defines how many times while
# loop has to be repeated
# Update statement, which updates condition"""

# while False:
#     print("Hello")

# # while 10&2:
# #     print("Hello")

# # while True:
#     # print("PYTHON") #in it python is print infinite times beacuse the condition never goes false

# # Write a program to find length of number (count of digits)
# num = int(input("Enter a number : "))
# count = 0
# while num>0:
#     num = num//10
#     count+=1
# print(f"Length of string {count}")

# # Write a program to print sum of digits of input number
# num = int(input("Enter a number : "))
# sum = 0
# while num>0:
#     r = num%10
#     sum += r
#     num = num//10
# print(f"Sum : {sum}")

# # In Python, an Armstrong number is a number that equals the sum of its individual digits, each raised to the power of the number of digits.
# # For example,
# # 153 is an Armstrong number because 1^3 + 5^3 + 3^3 equals 153
# # Write a program to find input 3 digit number is armstrong number or not

# num = int(input("Enter a 3 digit number "))
# num1 = num
# num2 = 0
# while num>0:
#     r = num % 10
#     num2 = num2 + (r**3)
#     num = num//10
# if num1 == num2:
#     print(f"Amstrong number")
# else:
#     print(f"Not Amstrong number")

# # Write a program to reverse input number
# num = int(input("Enter number :"))
# num1 = 0
# while num>0:
#     r = num%10
#     num1 = (num1*10)+r
#     num //= 10
# print(f"Reverse number : {num1}")

# Write a program to find input number is prime or not
num = int(input("Enter a number :"))
count=0
i=2
while i<num:
    if num%i==0:
        count+=1
    i=i+1
if count==0:
    print(f"{num} is prime")
else:
    print(f"{num} not is prime")