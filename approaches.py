# 🔑 Core Approaches to Solve DSA Problems
# 1. Brute Force
# Idea: Try all possible solutions without optimization.

# Use when: You need a baseline solution or have small constraints.

# Example: Find all pairs with a given sum.

# Count number of pairs with a given sum
def count_num(arr,target):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                count+=1
    return count
arr = [1,2,3,4,5,6]
target = 7
print(f"Count of pairs with sum {target} : {count_num(arr,target)}")


# Find first non-repeating character in a string
def first_non_repeating_char(s):
    ch = ''
    for i in s:
        if s.count(i) == 1:
            ch = i
            break
    return ch if ch else None
s = "swiss"
print(f"First non-repeating character in '{s}': {first_non_repeating_char(s)}")  # Output: 'w'


# Find duplicates in an array
def find_duplicates(arr):
    l1=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j] and arr[i] not in l1:
                l1.append(arr[i])
    return l1 if l1 else None
arr = [1, 2, 3, 4, 5, 6, 2, 3]
print(f"Duplicates in the array {arr}: {find_duplicates(arr)}")  # Output: [2, 3]


# Two Pointer Technique

# Check if array has a pair with target sum
def target_sum(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left<right:
        if arr[left]+arr[right] == target:
            return True
        elif arr[left]+arr[right] > target:
            right -= 1
        else:
            left += 1
    return False
arr = [1, 2, 3, 4, 5]
target = 3
print(f"Array {arr} has a pair with sum {target}: {target_sum(arr, target)}")  # Output: True


# Reverse a string or array in-place
def reverse_in_place(str):
    left = 0
    right = len(str) - 1
    while left<right:
        str[left],str[right]=str[right],str[left]
        left += 1
        right -= 1
    return str
s = "hello"
print(f"Reversed string '{s}': {''.join(reverse_in_place(list(s)))}")  # Output: 'olleh'


# Check if a string is a palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left<right:
        if s[left]!=s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "racecar"
s = "madam"
print(f"Is the string '{s}' a palindrome? {is_palindrome(s)}")  # Output: True

# Move Zeros to End
def move_zeros(arr):
    left = 0
    for right in range(len(arr)):
        if arr[right]!=0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    return arr
arr = [0, 1, 0, 3, 12]
arr = [0, 1, 0, 3, 12]
arr = [12, 0, 1, 0, 3]
print(f"Array after moving zeros to end: {move_zeros(arr)}")  # Output: [1, 3, 12, 0, 0]
