# 1. Generating Multiples
# Write a list comprehension that generates a list of the squares of all multiples of 3 from 1 to 30.

l1 = [num for num in range(1,31) if num%3==0]
print("Multiples of 3 : ",l1)

# 2. Flattening a Nested List
# Given a list of lists [[1, 2], [3, 4], [5, 6]], write a list comprehension to flatten it into a single list.

l1 = [[1, 2], [3, 4], [5, 6]]
l2 = [i for num in l1 for i in num]
print("Flatten list : ",l2)

# 3. Filtering with Conditions
# Using list comprehension, create a list of all even numbers from a given list nums = [10, 15, 20, 25, 30, 35] that are greater than 20.

nums = [10, 15, 20, 25, 30, 35]
even_nums = [num for num in nums if num%2==0 and num>20]
print("List of even nums : ",even_nums)

# 4. Extracting Dictionary Keys
# Given a dictionary data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}, write a list comprehension to generate a list of keys that have even values.

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
l1 = [key for key,val in data.items() if val%2==0]
print("List of Even keys : ",l1)

# 5. Using List Comprehension with Strings
# Write a list comprehension that extracts all the vowels from the string "intermediate level comprehension".

s = "intermediate level comprehension"
l1 = [ch for ch in s if ch in "AEIOUaeiou"]
print("List of Vowels : ",l1)

# 6. Prime Numbers using List Comprehension
# Using list comprehension, generate a list of all prime numbers between 10 and 50.

l1 = [num for num in range(10,51) if all(num%i!=0 for i in range(2,num))]
print("Prime Number List : ",l1)

# 7. Conditional Nested List Comprehension
# Create a 2D list using list comprehension where each element in the 3x3 matrix contains the sum of its row and column indices.

l1 = [[(i+j) for j in range(3)] for i in range(3)]
print("Nested List : ",l1)

# 9. Cartesian Product using List Comprehension
# Using two lists A = [1, 2] and B = ['a', 'b'], write a list comprehension to generate a Cartesian product as a list of tuples.

A = [1,2]
B = ['a','b']
l1 = [(i,j) for i in A for j in B]
print(l1)

# 10. Applying Functions within List Comprehensions
# Given a list of numbers [1, 4, 9, 16, 25], use a list comprehension to generate a new list containing the square roots of these numbers.
import math
sq = [1, 4, 9, 16, 25]
sqrt = [math.sqrt(num) for num in sq ]
print("sqrt : ",sqrt)