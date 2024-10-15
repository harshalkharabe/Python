#! Find the Second Largest Number in a List
# Write a Python program to find the second largest number in a list.
#----------- FIRST WAY --------------------#

list1 = [12,56,90,43,90,21]
max = max(list1)
smax = 0

for i in range(len(list1)):
    if max>list1[i]>smax:
        smax = list1[i]

print(f"Second largest in list is {smax}")

#======================================================================
# Write a Python program to find the second largest number in a list.
#----------------- SECOND WAY ---------------#

list1 = [12,56,90,43,90,21]
max = 0
smax = 0

for value in list1:
    if value > max:
        smax = max
        max = value
    elif max>value>smax:
        smax = value

print(f"Second largest value is {smax}")

#======================================================================
# Write a Python program to find the second largest number in a list.
#----------------- THIRD WAY ---------------#

list1 = [12,56,90,43,90,21]
max = 0
smax = 0

for val in list1:
    if val>max:
        max = val
for val in list1:
    if max>val>smax:
        smax = val

print(f"Second largest value is {smax}")

#======================================================#
# Write a Python function to find the common elements between two lists without using set operations.
#---------------- FIRST WAY ----------------#

l1 = [1,2,3,4]
l2 = [5,6,3,4]
l3 = []
for val in l1:
    if val in l2:
        l3.append(val)
print(f"{l1} and {l2}")
print(f"Common elements between them : {l3}")

# Write a Python function to find the common elements between two lists without using set operations.
#---------------- SECOND WAY ----------------#

l1 = [3,5,4]
l2 = [5,6,3,4]
l3 = []
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l3.append(l1[i])
print(f"{l1} and {l2}")
print(f"Common elements between them : {l3}")


#=====================================================================================
# Write a Python function that checks if a list of integers is sorted in ascending order. Return True if sorted, False otherwise.
#------------ FIRST WAY ----------------#

l1 = [1,2,6,4,3,9]
# l2 = l1
# print(l2)
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j] = l1[j],l1[i]
# print(l1)
bool = False
for i in range(len(l1)-1):
    if l1[i]>l1[i+1]:
        bool = False
        break
    else:
        bool = True
    
print(f"{l1} is sorted : {bool}")

#=====================================================================================
# Write a Python function that checks if a list of integers is sorted in ascending order. Return True if sorted, False otherwise.
#------------ SECOND WAY ----------------#

l1 = [1,2,3,4,9,5]
bool = l1 == sorted(l1)
# sorted(nums) returns a new list with the elements sorted in ascending order.
# The comparison nums == sorted(nums) checks if the original list is already sorted. If they are the same, it returns True; otherwise, it returns False.
print(f"{l1} is Sorted : {bool}")


#==============================================================================================
# Write a Python function that takes a list and returns a new list with all duplicate elements removed, keeping only the first occurrence of each element.
#------------------- FIRST WAY --------------#

l1 = [1,2,3,4,5,3,6,7,8,1]
l2 = []

for val in l1:
    if val not in l2:
        l2.append(val)
print(f"After removing duplicates : {l2}")

# Write a Python function that takes a list and returns a new list with all duplicate elements removed, keeping only the first occurrence of each element.
#------------------- SECOND WAY --------------#

l1 = [1,2,3,4,5,5,4,7,8,9]
l2 = set(l1)
print(f"After Removing Duplicates : {l2}")


#---------------------------------------------------------------------
# Write a Python program that takes a sentence as input and prints the words of the sentence in reverse order.

s = "python is owsome language"
print(s)
l1 = s.split(' ')
l2 = []
print(l1)
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
print(l2)
s1 = ' '.join(l2)
print(s1)


#---------------------------------------------------------------------
# Write a Python program that takes a sentence as input and prints the words of the sentence in reverse order.
#----------------- SECOND WAY -----------------------------------

s = "python is owsome language"
print(s)
l1 = s.split(' ')
s1 = l1[::-1]
s1 = ' '.join(s1)
print(f"Reverse string : {s1}")

#=======================================================================
# Write a Python program to find the sum of all even numbers in a given list.

l1 = [10,20,30,25,45]
s = 0
for i in l1:
    if i%2==0:
        s += i
print(f"Sum of even numbers in list is {s}")


#========================================================================
# Write a Python program that prints the first n numbers in the Fibonacci sequence using a for or while loop.
#------------FOR LOOP--------------------------------#
n = 10
n1 = 0
n2 = 1
n3 = 0
print(f"Fibonacci series : {n1} {n2}",end=' ')
for i in range(n):
    n3 = n1 + n2
    print(n3,end=' ')
    n1,n2 = n2,n3
print()

#========================================================================
# Write a Python program that prints the first n numbers in the Fibonacci sequence using a for or while loop.
#------------WHILE LOOP--------------------------------#
n = 10
n1 = 0
n2 = 1
n3 = 0
count = 0
print(f"Fibonacci series : {n1} {n2}",end=' ')
while count<n:
    n3 = n1 + n2
    print(n3,end=' ')
    n1,n2 = n2,n3
    count +=1 
print()

#=====================================================================
# Find the Unique Element Write a Python function that takes a list where every element appears twice except for one element, which appears only once. Return that unique element.

l1 = [1,33,3,2,4,1,4,2]
l2 = []
l = len(l1)-1
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            l2.append(l1[i])
print(l2)
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)

#========================================================================
#Write a Python function that takes two sorted lists and merges them into a single sorted list.
l1 = [1,23,3]
l2 = [2,4,6]
l3 = l1 + l2
print(l3)
for i in range(len(l3)):
    for j in range(i+1,len(l3)):
        if l3[i]>l3[j]:
            l3[i],l3[j]=l3[j],l3[i]
print(f'lists after merge and sorted {l3}')
print()

#================================================================================
# Write a Python function that checks if there are any duplicates in a list and returns True if there are, and False otherwise.
l1 = [1,2,3,4,5,11]
bool = False
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            bool=True
            break
print(f"{l1} contains duplicate elements : {bool}")

#==============================================================================
# Write a Python program that takes a string input and counts the number of vowels and consonants in it (ignore spaces and punctuation).
str1 = "Hello World!"
vcount,ccount=0,0
for i in str1:
    if i in "AEIOUaeiou":
        vcount += 1
    elif (i>='A' and i<='Z') or (i>='a' and i<='z'):
        ccount +=1
print(f"Vowels : {vcount} Consonent : {ccount}")

#===================================================================
# Write a python program to check the string is palandriom or not
s1 = "madam1"
s2 = ""
for i in s1[::-1]:
    s2 = s2+i
print(s2)
if s1==s2:
    print(f"it is a plandrom string {s2}")
else:
    print(f"it is not a plandrom string {s2}")

# Write a python program to check the string is palandriom or not
#-----------------Second Way----------------#

s1 = "madam"
s2 = s1[::-1]
ans = "Palandriom" if s1==s2 else "Not palandriom" 
print(ans)

# Write a python program to check the string is palandriom or not
s1 = ["racecar", "hello", "level", "world"]
s2 =[]
for i in range(len(s1)):
    s3 = ''
    for j in s1[i][::-1]:
        s3 = s3+j
    if s3==s1[i]:
        s2.append(s3)

#======================================================================e 
#Flatten a Nested List Write a Python function that takes a nested list and returns a flat list containing all the elements.

l1 = [[1, 2, [3, 4]], [5, 6], 7]
l2 = []
print(isinstance(l2,float))
for i in l1:
    if isinstance(i,list): # isinstance check karte ki jar i cha type list aasel tr true nhi tr false
        print(i,type(i))
        for j in i:
            print(j)
            if j is isinstance(j,list):
                l2.extend(j)
            else:
                l2.append(j)
    else:
        l2.append(i)
print(l2)

#================= SECOND WAY ============================
def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            # Recursively flatten the nested list
            flat_list.extend(flatten_list(element))
        else:
            # Append non-list elements directly
            flat_list.append(element)
    return flat_list

nested_list = [[1, 2, [3, 4]], [5, 6], 7]
result = flatten_list(nested_list)
print("Flattened List:", result)

#=============================================================================
#Convert decimal to binary
val = '0b'
num = 10
while num>0:
    r = num%2
    val = val + str(r)
    num//=2
print(val)


#====================================================================
# 
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# 
class Solution(object):
    def mergeAlternately(self, word1, word2):
        word3 = ''
        if len(word1)==len(word2):
            for i in range(len(word1)):
                word3 = word3 + (word1[i] + word2[i])
        elif len(word1)<len(word2):
            for i in range(len(word1)):
                word3 = word3 + (word1[i]+word2[i])
            else:
                print(word3)
                word3=word3+word2[len(word1):]
        else :
            for i in range(len(word2)):
                word3 = word3 + (word1[i]+word2[i])
            else:
                word3=word3+word1[len(word2):]
        return word3
a = Solution()

print(a.mergeAlternately("ab","pqrs"))

#==============================================================
# 
# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.
# 
# class Solution(object):
#     def findTheDifference(self, s, t):
#         for i in t:
#             if i not in s:
#                 return i

#================CHAT GPT SOLUTION======================#
from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        count_s = Counter(s)
        count_t = Counter(t)
        for char in count_t:
            if count_t[char] != count_s.get(char, 0):
                return char
a = Solution()
print(a.findTheDifference("a","aa"))

#========================================================================
# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

# Input: s = "anagram", t = "nagaram"
# Output: true
# class Solution(object):
#     def isAnagram(self, s, t):
#         a,b=0,0
#         for i in s:
#             a = a + ord(i)
        
#         for i in t:
#             b = b+ord(i)
        
#         if a==b:
#             return True
#         else:
#             return False

# class Solution(object):
#     def isAnagram(self, s, t):
#         return Counter(s) == Counter(t)

# a = Solution()
# print(a.isAnagram("Harshal","Ram"))
a = "Harshal"
print(Counter(a))


#========================================================================
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

class Solution(object):
    def plusOne(self, digits):
        s1 = ''
        for i in digits:
            s1=s1+str(i)
        n = int(s1)
        n += 1
        s2 = str(n)
        l1 = list(s2)
        l2 = []
        for i in l1:
            l2.append(int(i))
        return l2

a = Solution()
print(a.plusOne([1,2,3]))

#=================================================================
# Implement a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).


class Solution(object):
    def arraySign(self, nums):
        p = 1
        for i in nums:
            if i==0:
                return 0
            p *= i
        if p>0:
            return 1
        else:
            return -1

a = Solution()
print(a.arraySign([-1,3,-4,]))


#============================================================
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, arr):
        nums = arr
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
        return arr
    
#======================================================================
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
print()
print()
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1]-arr[0]
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1] != diff:
                return False
        else:
            return True

a = Solution()
print(a.canMakeArithmeticProgression([20,17,-18,-13,13,-14,-8,10,1,14,-19]))

#===========================================================================
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Input: nums = [1,2,2,3]
# Output: true
class Solution(object):
    def isMonotonic(self, nums):
        arr = nums
        if arr[0]>arr[1]:
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    if arr[i]>=arr[j]:
                        pass
                    else:
                        return False
            else:
                return True
        elif arr[0]<=arr[1]:
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    if arr[j]>=arr[i]:
                        pass
                    else:
                        return False    
            else:
                return True
        else:
            pass

#=========================CHATGPT===================================
def is_monotonic(nums):
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False  # Not decreasing
        if nums[i] < nums[i - 1]:
            increasing = False  # Not increasing

    return increasing or decreasing

# Example usage
nums = [1, 2, 2, 3]
print(is_monotonic(nums))  # Output: True

#===============================================================================
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

class Solution(object):
    def romanToInt(self, s1):
        s = 0
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        for i in range(len(s1)):
            if s1[i] == "I":
                if "X" in s1[i+1:]:
                    X = 9
                elif "V" in s1[i+1:]:
                    V = 4
                else:
                    s += I
            elif s1[i]=="V":
                s += V
            elif s1[i]=="X":
                if "L" in s1[i+1:]:
                    L= 40
                elif "C" in s1[i+1:]:
                    C = 90
                else:
                    s += X
            elif s1[i]=="L":
                s += L
            elif s1[i]=="C":
                if "D" in s1[i+1:]:
                    D = 400
                elif "M" in s1[i+1:]:
                    M = 900
                else:
                    s += C
            elif s1[i]=="D":
                s += D
            elif s1[i]=="M":
                s += M
            else:
                s += 0
        return s
        
# #======================================================================
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal 
# substring
#  consisting of non-space characters only.
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

class Solution(object):
    def lengthOfLastWord(self, s):
        l1 = s.split()
        for i in l1:
            length = len(i)
        return length

a = Solution()
# print(a.lengthOfLastWord("Harshal Kharabe"))

#==================================================================
print(sep='\n\n')
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

class Solution(object):
    @staticmethod
    def is_integer(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    def calPoints(self, operations):
        l1 = []
        s = 0
        for i in operations:
            if Solution.is_integer(i):
                i = int(i)
                l1.append(i)
            elif i == "+":
                if len(l1)>=2:
                    s = l1[-1]+l1[-2]
                    l1.append(s)
                else:
                    s = l1[-1]
                    l1.append(s)
            elif i == 'D':
                p = l1[-1]*2
                l1.append(p)
            elif i == 'C':
                del l1[-1]
            else :
                pass
        s1 = sum(l1)
        return s1

a = Solution()
print(a.calPoints(["5","2","C","D","+"]))
