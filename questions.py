# #! Find the Second Largest Number in a List
# # Write a Python program to find the second largest number in a list.
# #----------- FIRST WAY --------------------#

# list1 = [12,56,90,43,90,21]
# max = max(list1)
# smax = 0

# for i in range(len(list1)):
#     if max>list1[i]>smax:
#         smax = list1[i]

# print(f"Second largest in list is {smax}")

# #======================================================================
# # Write a Python program to find the second largest number in a list.
# #----------------- SECOND WAY ---------------#

# list1 = [12,56,90,43,90,21]
# max = 0
# smax = 0

# for value in list1:
#     if value > max:
#         smax = max
#         max = value
#     elif max>value>smax:
#         smax = value

# print(f"Second largest value is {smax}")

# #======================================================================
# # Write a Python program to find the second largest number in a list.
# #----------------- THIRD WAY ---------------#

# list1 = [12,56,90,43,90,21]
# max = 0
# smax = 0

# for val in list1:
#     if val>max:
#         max = val
# for val in list1:
#     if max>val>smax:
#         smax = val

# print(f"Second largest value is {smax}")

# #======================================================#
# # Write a Python function to find the common elements between two lists without using set operations.
# #---------------- FIRST WAY ----------------#

# l1 = [1,2,3,4]
# l2 = [5,6,3,4]
# l3 = []
# for val in l1:
#     if val in l2:
#         l3.append(val)
# print(f"{l1} and {l2}")
# print(f"Common elements between them : {l3}")

# # Write a Python function to find the common elements between two lists without using set operations.
# #---------------- SECOND WAY ----------------#

# l1 = [3,5,4]
# l2 = [5,6,3,4]
# l3 = []
# for i in range(len(l1)):
#     for j in range(len(l2)):
#         if l1[i]==l2[j]:
#             l3.append(l1[i])
# print(f"{l1} and {l2}")
# print(f"Common elements between them : {l3}")


# #=====================================================================================
# # Write a Python function that checks if a list of integers is sorted in ascending order. Return True if sorted, False otherwise.
# #------------ FIRST WAY ----------------#

# l1 = [1,2,6,4,3,9]
# # l2 = l1
# # print(l2)
# # for i in range(len(l1)):
# #     for j in range(i+1,len(l1)):
# #         if l1[i]>l1[j]:
# #             l1[i],l1[j] = l1[j],l1[i]
# # print(l1)
# bool = False
# for i in range(len(l1)-1):
#     if l1[i]>l1[i+1]:
#         bool = False
#         break
#     else:
#         bool = True
    
# print(f"{l1} is sorted : {bool}")

# #=====================================================================================
# # Write a Python function that checks if a list of integers is sorted in ascending order. Return True if sorted, False otherwise.
# #------------ SECOND WAY ----------------#

# l1 = [1,2,3,4,9,5]
# bool = l1 == sorted(l1)
# # sorted(nums) returns a new list with the elements sorted in ascending order.
# # The comparison nums == sorted(nums) checks if the original list is already sorted. If they are the same, it returns True; otherwise, it returns False.
# print(f"{l1} is Sorted : {bool}")


# #==============================================================================================
# # Write a Python function that takes a list and returns a new list with all duplicate elements removed, keeping only the first occurrence of each element.
# #------------------- FIRST WAY --------------#

# l1 = [1,2,3,4,5,3,6,7,8,1]
# l2 = []

# for val in l1:
#     if val not in l2:
#         l2.append(val)
# print(f"After removing duplicates : {l2}")

# # Write a Python function that takes a list and returns a new list with all duplicate elements removed, keeping only the first occurrence of each element.
# #------------------- SECOND WAY --------------#

# l1 = [1,2,3,4,5,5,4,7,8,9]
# l2 = set(l1)
# print(f"After Removing Duplicates : {l2}")


# #---------------------------------------------------------------------
# # Write a Python program that takes a sentence as input and prints the words of the sentence in reverse order.

# s = "python is owsome language"
# print(s)
# l1 = s.split(' ')
# l2 = []
# print(l1)
# for i in range(len(l1)-1,-1,-1):
#     l2.append(l1[i])
# print(l2)
# s1 = ' '.join(l2)
# print(s1)


# #---------------------------------------------------------------------
# # Write a Python program that takes a sentence as input and prints the words of the sentence in reverse order.
# #----------------- SECOND WAY -----------------------------------

# s = "python is owsome language"
# print(s)
# l1 = s.split(' ')
# s1 = l1[::-1]
# s1 = ' '.join(s1)
# print(f"Reverse string : {s1}")

# #=======================================================================
# # Write a Python program to find the sum of all even numbers in a given list.

# l1 = [10,20,30,25,45]
# s = 0
# for i in l1:
#     if i%2==0:
#         s += i
# print(f"Sum of even numbers in list is {s}")


# #========================================================================
# # Write a Python program that prints the first n numbers in the Fibonacci sequence using a for or while loop.
# #------------FOR LOOP--------------------------------#
# n = 10
# n1 = 0
# n2 = 1
# n3 = 0
# print(f"Fibonacci series : {n1} {n2}",end=' ')
# for i in range(n):
#     n3 = n1 + n2
#     print(n3,end=' ')
#     n1,n2 = n2,n3
# print()

# #========================================================================
# # Write a Python program that prints the first n numbers in the Fibonacci sequence using a for or while loop.
# #------------WHILE LOOP--------------------------------#
# n = 10
# n1 = 0
# n2 = 1
# n3 = 0
# count = 0
# print(f"Fibonacci series : {n1} {n2}",end=' ')
# while count<n:
#     n3 = n1 + n2
#     print(n3,end=' ')
#     n1,n2 = n2,n3
#     count +=1 
# print()

# #=====================================================================
# # Find the Unique Element Write a Python function that takes a list where every element appears twice except for one element, which appears only once. Return that unique element.

# l1 = [1,33,3,2,4,1,4,2]
# l2 = []
# l = len(l1)-1
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]==l1[j]:
#             l2.append(l1[i])
# print(l2)
# l3=[]
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print(l3)

# #========================================================================
# #Write a Python function that takes two sorted lists and merges them into a single sorted list.
# l1 = [1,23,3]
# l2 = [2,4,6]
# l3 = l1 + l2
# print(l3)
# for i in range(len(l3)):
#     for j in range(i+1,len(l3)):
#         if l3[i]>l3[j]:
#             l3[i],l3[j]=l3[j],l3[i]
# print(f'lists after merge and sorted {l3}')
# print()

# #================================================================================
# # Write a Python function that checks if there are any duplicates in a list and returns True if there are, and False otherwise.
# l1 = [1,2,3,4,5,11]
# bool = False
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]==l1[j]:
#             bool=True
#             break
# print(f"{l1} contains duplicate elements : {bool}")

# #==============================================================================
# # Write a Python program that takes a string input and counts the number of vowels and consonants in it (ignore spaces and punctuation).
# str1 = "Hello World!"
# vcount,ccount=0,0
# for i in str1:
#     if i in "AEIOUaeiou":
#         vcount += 1
#     elif (i>='A' and i<='Z') or (i>='a' and i<='z'):
#         ccount +=1
# print(f"Vowels : {vcount} Consonent : {ccount}")

# #===================================================================
# # Write a python program to check the string is palandriom or not
# s1 = "madam1"
# s2 = ""
# for i in s1[::-1]:
#     s2 = s2+i
# print(s2)
# if s1==s2:
#     print(f"it is a plandrom string {s2}")
# else:
#     print(f"it is not a plandrom string {s2}")

# # Write a python program to check the string is palandriom or not
# #-----------------Second Way----------------#

# s1 = "madam"
# s2 = s1[::-1]
# ans = "Palandriom" if s1==s2 else "Not palandriom" 
# print(ans)

# # Write a python program to check the string is palandriom or not
# s1 = ["racecar", "hello", "level", "world"]
# s2 =[]
# for i in range(len(s1)):
#     s3 = ''
#     for j in s1[i][::-1]:
#         s3 = s3+j
#     if s3==s1[i]:
#         s2.append(s3)

# #======================================================================e 
# #Flatten a Nested List Write a Python function that takes a nested list and returns a flat list containing all the elements.

# l1 = [[1, 2, [3, 4]], [5, 6], 7]
# l2 = []
# print(isinstance(l2,float))
# for i in l1:
#     if isinstance(i,list): # isinstance check karte ki jar i cha type list aasel tr true nhi tr false
#         print(i,type(i))
#         for j in i:
#             print(j)
#             if j is isinstance(j,list):
#                 l2.extend(j)
#             else:
#                 l2.append(j)
#     else:
#         l2.append(i)
# print(l2)

# #================= SECOND WAY ============================
# def flatten_list(nested_list):
#     flat_list = []
#     for element in nested_list:
#         if isinstance(element, list):
#             # Recursively flatten the nested list
#             flat_list.extend(flatten_list(element))
#         else:
#             # Append non-list elements directly
#             flat_list.append(element)
#     return flat_list

# nested_list = [[1, 2, [3, 4]], [5, 6], 7]
# result = flatten_list(nested_list)
# print("Flattened List:", result)

# #=============================================================================
# #Convert decimal to binary
# val = '0b'
# num = 10
# while num>0:
#     r = num%2
#     val = val + str(r)
#     num//=2
# print(val)


# #====================================================================
# # 
# # Input: word1 = "abc", word2 = "pqr"
# # Output: "apbqcr"
# # Explanation: The merged string will be merged as so:
# # word1:  a   b   c
# # word2:    p   q   r
# # merged: a p b q c r
# # 
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         word3 = ''
#         if len(word1)==len(word2):
#             for i in range(len(word1)):
#                 word3 = word3 + (word1[i] + word2[i])
#         elif len(word1)<len(word2):
#             for i in range(len(word1)):
#                 word3 = word3 + (word1[i]+word2[i])
#             else:
#                 print(word3)
#                 word3=word3+word2[len(word1):]
#         else :
#             for i in range(len(word2)):
#                 word3 = word3 + (word1[i]+word2[i])
#             else:
#                 word3=word3+word1[len(word2):]
#         return word3
# a = Solution()

# print(a.mergeAlternately("ab","pqrs"))

# #==============================================================
# # 
# # You are given two strings s and t.
# # String t is generated by random shuffling string s and then add one more letter at a random position.
# # Return the letter that was added to t.
# # 
# # class Solution(object):
# #     def findTheDifference(self, s, t):
# #         for i in t:
# #             if i not in s:
# #                 return i

# #================CHAT GPT SOLUTION======================#
# from collections import Counter
# class Solution(object):
#     def findTheDifference(self, s, t):
#         count_s = Counter(s)
#         count_t = Counter(t)
#         for char in count_t:
#             if count_t[char] != count_s.get(char, 0):
#                 return char
# a = Solution()
# print(a.findTheDifference("a","aa"))

# #========================================================================
# # Given two strings s and t, return true if t is an 
# # anagram
# #  of s, and false otherwise.

# # Input: s = "anagram", t = "nagaram"
# # Output: true
# # class Solution(object):
# #     def isAnagram(self, s, t):
# #         a,b=0,0
# #         for i in s:
# #             a = a + ord(i)
        
# #         for i in t:
# #             b = b+ord(i)
        
# #         if a==b:
# #             return True
# #         else:
# #             return False

# # class Solution(object):
# #     def isAnagram(self, s, t):
# #         return Counter(s) == Counter(t)

# # a = Solution()
# # print(a.isAnagram("Harshal","Ram"))
# a = "Harshal"
# print(Counter(a))


# #========================================================================
# # You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# # Increment the large integer by one and return the resulting array of digits.
# # Example 1:
# # Input: digits = [1,2,3]
# # Output: [1,2,4]
# # Explanation: The array represents the integer 123.
# # Incrementing by one gives 123 + 1 = 124.
# # Thus, the result should be [1,2,4].

# class Solution(object):
#     def plusOne(self, digits):
#         s1 = ''
#         for i in digits:
#             s1=s1+str(i)
#         n = int(s1)
#         n += 1
#         s2 = str(n)
#         l1 = list(s2)
#         l2 = []
#         for i in l1:
#             l2.append(int(i))
#         return l2

# a = Solution()
# print(a.plusOne([1,2,3]))

# #=================================================================
# # Implement a function signFunc(x) that returns:
# # 1 if x is positive.
# # -1 if x is negative.
# # 0 if x is equal to 0.
# # You are given an integer array nums. Let product be the product of all values in the array nums.
# # Return signFunc(product).


# class Solution(object):
#     def arraySign(self, nums):
#         p = 1
#         for i in nums:
#             if i==0:
#                 return 0
#             p *= i
#         if p>0:
#             return 1
#         else:
#             return -1

# a = Solution()
# print(a.arraySign([-1,3,-4,]))


# #============================================================
# # Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# # Note that you must do this in-place without making a copy of the array.
# # Input: nums = [0,1,0,3,12]
# # Output: [1,3,12,0,0]

# class Solution(object):
#     def moveZeroes(self, arr):
#         nums = arr
#         non_zero_index = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
#                 non_zero_index += 1
#         return arr
    
# #======================================================================
# # A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# # Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

# # Input: arr = [3,5,1]
# # Output: true
# # Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
# print()
# print()
# class Solution(object):
#     def canMakeArithmeticProgression(self, arr):
#         arr.sort()
#         diff = arr[1]-arr[0]
#         for i in range(2,len(arr)):
#             if arr[i]-arr[i-1] != diff:
#                 return False
#         else:
#             return True

# a = Solution()
# print(a.canMakeArithmeticProgression([20,17,-18,-13,13,-14,-8,10,1,14,-19]))

# #===========================================================================
# # An array is monotonic if it is either monotone increasing or monotone decreasing.
# # An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# # Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# # Input: nums = [1,2,2,3]
# # Output: true
# class Solution(object):
#     def isMonotonic(self, nums):
#         arr = nums
#         if arr[0]>arr[1]:
#             for i in range(len(arr)):
#                 for j in range(i+1,len(arr)):
#                     if arr[i]>=arr[j]:
#                         pass
#                     else:
#                         return False
#             else:
#                 return True
#         elif arr[0]<=arr[1]:
#             for i in range(len(arr)):
#                 for j in range(i+1,len(arr)):
#                     if arr[j]>=arr[i]:
#                         pass
#                     else:
#                         return False    
#             else:
#                 return True
#         else:
#             pass

# #=========================CHATGPT===================================
# def is_monotonic(nums):
#     increasing = decreasing = True

#     for i in range(1, len(nums)):
#         if nums[i] > nums[i - 1]:
#             decreasing = False  # Not decreasing
#         if nums[i] < nums[i - 1]:
#             increasing = False  # Not increasing

#     return increasing or decreasing

# # Example usage
# nums = [1, 2, 2, 3]
# print(is_monotonic(nums))  # Output: True

# #===============================================================================
# # Symbol       Value
# # I             1
# # V             5
# # X             10
# # L             50
# # C             100
# # D             500
# # M             1000
# # Input: s = "III"
# # Output: 3
# # Explanation: III = 3.

# class Solution(object):
#     def romanToInt(self, s1):
#         s = 0
#         I = 1
#         V = 5
#         X = 10
#         L = 50
#         C = 100
#         D = 500
#         M = 1000
#         for i in range(len(s1)):
#             if s1[i] == "I":
#                 if "X" in s1[i+1:]:
#                     X = 9
#                 elif "V" in s1[i+1:]:
#                     V = 4
#                 else:
#                     s += I
#             elif s1[i]=="V":
#                 s += V
#             elif s1[i]=="X":
#                 if "L" in s1[i+1:]:
#                     L= 40
#                 elif "C" in s1[i+1:]:
#                     C = 90
#                 else:
#                     s += X
#             elif s1[i]=="L":
#                 s += L
#             elif s1[i]=="C":
#                 if "D" in s1[i+1:]:
#                     D = 400
#                 elif "M" in s1[i+1:]:
#                     M = 900
#                 else:
#                     s += C
#             elif s1[i]=="D":
#                 s += D
#             elif s1[i]=="M":
#                 s += M
#             else:
#                 s += 0
#         return s
        
# # #======================================================================
# # Given a string s consisting of words and spaces, return the length of the last word in the string.
# # A word is a maximal 
# # substring
# #  consisting of non-space characters only.
# # Input: s = "Hello World"
# # Output: 5
# # Explanation: The last word is "World" with length 5.

# class Solution(object):
#     def lengthOfLastWord(self, s):
#         l1 = s.split()
#         for i in l1:
#             length = len(i)
#         return length

# a = Solution()
# # print(a.lengthOfLastWord("Harshal Kharabe"))

# #==================================================================
# print(sep='\n\n')
# # You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# # You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# # An integer x.
# # Record a new score of x.
# # '+'.
# # Record a new score that is the sum of the previous two scores.
# # 'D'.
# # Record a new score that is the double of the previous score.
# # 'C'.
# # Invalidate the previous score, removing it from the record.
# # Return the sum of all the scores on the record after applying all the operations.
# # The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

# # Input: ops = ["5","2","C","D","+"]
# # Output: 30
# # Explanation:
# # "5" - Add 5 to the record, record is now [5].
# # "2" - Add 2 to the record, record is now [5, 2].
# # "C" - Invalidate and remove the previous score, record is now [5].
# # "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# # "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# # The total sum is 5 + 10 + 15 = 30.

# class Solution(object):
#     @staticmethod
#     def is_integer(s):
#         try:
#             int(s)
#             return True
#         except ValueError:
#             return False
#     def calPoints(self, operations):
#         l1 = []
#         s = 0
#         for i in operations:
#             if Solution.is_integer(i):
#                 i = int(i)
#                 l1.append(i)
#             elif i == "+":
#                 if len(l1)>=2:
#                     s = l1[-1]+l1[-2]
#                     l1.append(s)
#                 else:
#                     s = l1[-1]
#                     l1.append(s)
#             elif i == 'D':
#                 p = l1[-1]*2
#                 l1.append(p)
#             elif i == 'C':
#                 del l1[-1]
#             else :
#                 pass
#         s1 = sum(l1)
#         return s1

# a = Solution()
# print(a.calPoints(["5","2","C","D","+"]))


# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         l1 = []
#         n1 = nums1
#         n2 = nums2
#         for i in range(m):
#             l1.append(n1[i])
#         for j in range(n):
#             l1.append(n2[j])
#         l1.sort()
#         return l1
        
# a = Solution()
# print(a.merge([0],0,[1],1))

# #===============================================
# # Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
# # Input: s = "abab"
# # Output: true
# # Explanation: It is the substring "ab" twice.

# def repeatedSubstringPattern(s):
#     doubled = (s + s)[1:-1]  # Remove first and last character from s + s
#     return s in doubled


# #================================================================================
# # Input: nums = [0,0,1,1,1,1,2,3,3]
# # Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# # Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# # It does not matter what you leave beyond the returned k (hence they are underscores).

# class Solution(object):
#     def removeDuplicates(self, nums):
#         num = []
#         for i in nums:
#             if i not in num:
#                 num.append(i)
#         c = []
#         for i in num:
#             x = nums.count(i)
#             c.append(x)
#         c.sort()
#         for i in nums:
#             while True:
#                 if nums.count(i)>2:
#                     nums.remove(i)
#                 else:
#                     break

#         return len(nums)
        
# a = Solution()
# print(a.removeDuplicates([0,0,1,1,1,1,2,3,3]))

# #=====================================================================================
# # Input: accounts = [[1,2,3],[3,2,1]]
# # Output: 6
# # Explanation:
# # 1st customer has wealth = 1 + 2 + 3 = 6
# # 2nd customer has wealth = 3 + 2 + 1 = 6
# # Both customers are considered the richest with a wealth of 6 each, so return 6.

# class Solution(object):
#     def maximumWealth(self, accounts):
#         total = 0
#         for i in accounts:
#             if sum(i)>total:
#                 total = sum(i)
#         return total
        
# a = Solution()
# print(a.maximumWealth([[1,2,3],[3,2,1]]))

# #=================================================================
# # Input: mat = [[1,2,3],
# #               [4,5,6],
# #               [7,8,9]]
# # Output: 25
# # Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# # Notice that element mat[1][1] = 5 is counted only once.

# mat =  [[7,3,1,9],
#         [3,4,6,9],
#         [6,9,6,6],
#         [9,5,8,5]]
# class Solution(object):
#     def diagonalSum(self, mat):
#         sum = 0
#         for i in range(len(mat)):
#             for j in range(len(mat)):
#                 if i==j:
#                     sum = sum + mat[i][j]
#         for i in range(-1,-(len(mat)+1),-1):
#             for j in range(len(mat)):
#                 if i==-(j+1):
#                     sum = sum + mat[i][j]

#         if len(mat)%2==0:
#             return sum
#         else:
#             l = len(mat)//2
#             sum = sum - mat[l][l]
#             return sum
# a = Solution()
# print("Sum of Diagonal elements : ",a.diagonalSum(mat))

# #========================================================================
# # Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# # class Solution(object):
# #     def spiralOrder(self, matrix):
        

# # a = Solution()
# # print(a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


# #==========================================================
# # Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# l1 = [[0],[1]]
# row,col = None,None
# for i in range(len(l1)):
#     for j in range(len(l1[i])):
#         if l1[i][j] == 0:
#             row = i
#             col = j
# print(row,col)
# if row != None and col != None:
#     for i in range(len(l1)):
#         for j in range(len(l1[i])):
#             if i==row:
#                 l1[row][j] = 0
#             if j==col:
#                 l1[i][col]=0
#             if j==row:
#                 l1[i][row]=0
# print(l1)

# #===================SECOND WAY=========================
# # def setZeroes(matrix):
# #     rows_to_zero = set()
# #     cols_to_zero = set()

# #     # Identify rows and columns to be zeroed
# #     for i in range(len(matrix)):
# #         for j in range(len(matrix[0])):
# #             if matrix[i][j] == 0:
# #                 rows_to_zero.add(i)
# #                 cols_to_zero.add(j)

# #     # Set the identified rows to 0
# #     for row in rows_to_zero:
# #         for j in range(len(matrix[0])):
# #             matrix[row][j] = 0

# #     # Set the identified columns to 0
# #     for col in cols_to_zero:
# #         for i in range(len(matrix)):
# #             matrix[i][col] = 0

# #     return matrix

# # # Example usage
# # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# # result = setZeroes(matrix)
# # print(result)


# #===============================================================================
# # from collections import Counter
# # class Solution(object):
# #     def majorityElement(self, nums):
# #         counter = Counter(nums)
# #         return max(counter, key=counter.get)



# class Solution(object):
#     def rotate(self, nums, k):
#         for i in range(k):
#             item = nums.pop()
#             nums.insert(0,item)
#         return nums
        
# a = Solution()
# print(a.rotate([1,2,3,4,5,6,7],3))

#====================================================================================
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

class Solution(object):
    def average(self, salary):
        min_salary = min(salary)
        max_salary = max(salary)
        total_sum = sum(salary) - min_salary - max_salary
        average = total_sum / (len(salary) - 2)
        return average
        

a = Solution()
avg = a.average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000])
print(f"Average : {avg:.5f}")

#=======================================================
# Best Time to Buy and Sell Stock - 1

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf') 
        max_profit = 0 
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
    
#------------------------------------------------------------------------
# Best Time to Buy and Sell Stock - 2
class Solution(object):
    def maxProfit(self, prices):
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        return total_profit

#========================================================================
# Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        l1 = s.split()
        l2 = l1[::-1]
        s1 = " ".join(l2)
        return s1

a = Solution()
print(a.reverseWords("the sky is blue"))

#===============================================================================
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution(object):
    def strStr(self, haystack, needle):
        lh = len(haystack)
        ln = len(needle)
        val = -1
        for i in range(lh):
            print(haystack[i:i+ln])
            print(needle[:])
            if haystack[i:i+ln]==needle[:]:
                val = i
                break
        return val
           
a = Solution()
print(a.strStr("abc","c"))

#=============================CHAT GPT========================================
class Solution(object):
    def canJump(self,nums):
        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
            print(furthest)
            if furthest >= len(nums) - 1:
                return True
        return False

a = Solution()
print(a.canJump([2,3,1,1,4]))
print(a.canJump([3,2,1,0,4]))

#==============================================================
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
def fun(strs):
    if not strs:
            return ""
    
    prefix = strs[0]
    
    for string in strs[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
    
    return prefix

# 46. Write a Python program to select the odd items of a list. 
l1 = list(range(5,51,5))
l2 = [num for num in l1 if num%2!=0]
print(l1,l2,sep='\n')

# 47. Write a Python program to insert an element before each element of a list.
# l1 = [12,34,56,78,89]
# l2 = []
# for i in range(len(l1)):
#     l2.append(l1[i])
#     item = int(input(f"Enter number to insert at place :"))
#     l2.append(item)

# print(l2)

# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function. 
l1 = [[1,2],[3,4],[5,6],[7,8]]
print(l1)
for i in l1:
    print(i)

# 49. Write a Python program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

l1 = ["Black", "Red", "Maroon", "Yellow"]
l2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
color = []
for i in range(len(l1)):
    dic = {}
    dic['color_name'] = l1[i]
    dic['color_code'] = l2[i]
    color.append(dic)
print(color)

# 50. Write a Python program to sort a list of nested dictionaries. 
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 20}
]
print(f"Before sorting : {data}")
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]['age']>data[j]['age']:
            data[i],data[j]=data[j],data[i]
print("After Sorting : ",data)