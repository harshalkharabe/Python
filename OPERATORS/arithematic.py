"""Arithmetic Operators
Arithmetic operators are binary operators and these operators required 2
operands. These operators are used to create arithmetic expression.

Operator    Description
+           Addition or Concatenation of sequences
-           Subtracting
*           Multiplication and Repeating of sequence
/           Float division
//          Floor division
%           Modulo
**          Power of"""

print("Sum of integers : ",2+5)
print("Sum of float : ",2.9+5.3)
print("Sum of complex : ",(3+4j)+(5+7j))
print("Sum of boolean : ",True+True)
print("Sum of boolean : ",True+False)
print("Sum of values : ",1.5+False+32)

#Concantination

print("Concantination of string : ")
print("Harshal"+"Kharabe")
print("Concantication of list : ",[89,32,45,43]+[1,2,3,4])

# Write a program to input name, 3 subject marks and caculate total marks

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

print("Total : ",num1+num2+num3)


# Example of – Operator
print("Difference of two integers ",10-5)
print("Difference of two floats ",1.5-1.0)
print("Difference of two complex ",1+2j-1+1j)
print("Difference of boolean ",True-False)
print("Difference of boolean ",False-True)
print("Difference of values ",10-True)
print("Difference of values ",10-1.5)

# Output
# Difference of two integers 5
# Difference of two floats 0.5
# Difference of two complex 3j
# Difference of boolean 1
# Difference of boolean 0
# Difference of values 9
# Difference of values 8.5

# Write a program to input two distances and find difference
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))

print(f"Difference is {num1-num2}")

# Write a program to swap two numbers
# num1 = int(input("Enter number : "))
# num2 = int(input("Enter number : "))

# num3 = num1
# num1 = num2
# num2 = num3
# print(f"After Swaping num1 = {num1} num2 = {num2}")

# num1 = int(input("Enter number : "))
# num2 = int(input("Enter number : "))

# num1 = num1+num2
# num2 = num1-num2
# num1 = num1-num2

# print(f"After Swaping num1 = {num1} num2 = {num2}")

num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))

num1,num2 = num2,num1

print(f"After Swaping num1 = {num1} num2 = {num2}")