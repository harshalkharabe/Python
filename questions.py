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

# Input: sentence = "leetcode exercises sound delightful"
# Output: true
# Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
# - leetcode's last character is equal to exercises's first character.
# - exercises's last character is equal to sound's first character.
# - sound's last character is equal to delightful's first character.
# - delightful's last character is equal to leetcode's first character.
# The sentence is circular.

class Solution(object):
    def isCircularSentence(self, sentence):
        l1 = sentence.split(" ")
        if len(l1)==1:
            if l1[0][-1]==l1[0][0]:
                return True
            else:
                return False
        for i in range(len(l1)-1):
            if l1[i][-1]==l1[i+1][0]:
                pass
            else:
                return False
        return True
        
a = Solution()
print("Ans : ",a.isCircularSentence("leetcode"))
maxsum = float('-inf')
l1 = [-2,-1]
for i in range(len(l1)):
    currentsum = 0
    for j in range(i,len(l1)):
        currentsum += l1[j]
        maxsum = max(currentsum,maxsum)
        if currentsum<0:
            currentsum=0
print("Maxsum :",maxsum)

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1

# max_water = 0
# for i in range(len(height)):
#     for j in range(i+1,len(height)):
#         b = j-i
#         h = min(height[i],height[j])
#         total_water = h*b
#         max_water = max(max_water,total_water)
#         # if total_water>max_water:
#         #     max_water=total_water
# print(max_water)

height = [1,8,6,2,5,4,8,3,7]
mwater=0
lb=0
rb=len(height)-1
while lb<rb:
    b = rb-lb
    h = min(height[lb],height[rb])
    twater = h*b
    mwater = max(twater,mwater)
    if height[lb]<height[rb]:
        lb+=1
    else:
        rb-=1
print(mwater)

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
nums = [-1,1,0,-3,3]
# l1=[]
# for i in range(len(nums)):
#     m=1
#     for j in range(len(nums)):
#         if i==j:
#             pass
#         else:
#             m*=nums[j]
#     l1.append(m)
# print(l1)


class Solution(object):
    def compressedString(self, word):
        s = ""
        i=0
        while i<len(word):
            ch = word[i]
            c = 0
            while i<len(word) and word[i]==ch and c<9:
                c+=1
                i+=1
            s += str(c)+ch
        return s


a = Solution()
print(a.compressedString("aaaaaaaaaaaaaabb"))


# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = "A man, a plan, a canal: Panama"
s='0P'
s1 = ''
for i in range(len(s)):
    if (s[i]>="A" and s[i]<='Z') or (s[i]>='a' and s[i]<='z'):
        s1 += s[i].lower()
    elif (s[i]>='0' and s[i]<='9'):
        s1+=s[i]
print(s1==s1[::-1])

s = "axc"
t = "ahbgdc"
# Output: false


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,6,9,8,7,4,5]
srow = 0
erow = len(matrix)-1
scol = 0
ecol = len(matrix[0])-1
op = []
while srow<=erow and scol<=ecol:
    #top row
    for i in range(scol,ecol+1):
        op.append(matrix[srow][i])

    #right col
    for i in range(srow+1,erow+1):
        op.append(matrix[i][ecol])

    #down row
    for i in range(ecol-1,scol-1,-1):
        if srow==erow:
            break
        op.append(matrix[erow][i])

    #left col
    for i in range(erow-1,srow,-1):
        if scol==ecol:
            break
        op.append(matrix[i][scol])

    srow+=1
    erow-=1
    ecol-=1
    scol+=1
print(op)


words = ["Hello","Alaska","Dad","Peace"]
res = []
for i in words:
    print(i)
    l1 = [ch for ch in i if ch.lower() in "qwertyuiop"]
    s1 = ''.join(l1)
    l2 = [ch for ch in i if ch.lower() in "asdfghjkl"]
    s2 = ''.join(l2)
    l3 = [ch for ch in i if ch.lower() in "zxcvbnm"]
    s3 = ''.join(l3)
    print(s1,s2,s3)
    if i==s1 or i==s2 or i==s3:
        res.append(i)
print(res)

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# list1 = ["happy","sad","good"]
# list2 = ["sad","happy","good"]
# l3 = []
# least_index = len(list1)
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i]==list2[j]:
#             idx = sum(i,j)
#             least_index = min(least_index,idx)

l1 = ["cd","ac","dc","ca","zz"]
for i in range(len(l1)):
    if l1[i][::-1] in l1[i:] and l1[i][::-1]!=l1[i]:
        print(l1[i])

print('ab' in 'baa')


def minimizedMaximum( n, quantities):
        total = sum(quantities)
        op = total/n
        return round(op)

n = 6
quantities = [11,6]
# n = 7
# quantities = [15,10,10]
print(minimizedMaximum(n,quantities))



c=0
strs=["zyx","wvu","tsr"]
for i in strs:
    if i == "".join(sorted(i)):
        print("h")
        c+=1
        # return c
print(c)

print([1,3]+[2])

l1 = [1,2,3]
print(1 in l1)

a = int("-3")
print(a)


# s={'a','b'}
# s1 = "".join(s)
# print(s,s1)
# print("cb"=="bc")
s="saak"
# print(s.count("a"))


l1 = [-1,0,1,2,-1,-4]
l2=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        for k in range(j+1,len(l1)):
            if l1[i]+l1[j]+l1[k]==0:
                nums = [l1[i],l1[j],l1[k]]
                nums.sort()
                if nums not in l2:
                    l2.append(nums)
print(l2)

# for i in range(len(l1)):
#     a = -l1[i]
#     for j in range(i+1,len(l1)):
#         c = a - l1[j]
        
# print(l2)
l1 = [-1,0,1,2,-1,-4]
l2=[]
l1.sort()
for i in range(len(l1)):
    j = i+1
    k = len(l1)-1
    if i>0 and l1[i]==l1[i-1]:continue
    while j<k:
        sum = l1[i]+l1[j]+l1[k]
        if sum<0:
            j=j+1
        elif sum>0:
            k-=1
        else:
            l2.append([l1[i],l1[j],l1[k]])
            j+=1
            k-=1

            while j<k and l1[j]==l1[j-1]:j+=1
        
print(l2)


#next permutation
l1 = [1,3,2]
n = len(l1)-1
piv = -1
for i in range(n-1,-1,-1):
    if l1[i]<l1[i+1]:
        piv = i
        break
if piv==-1:
    l1.reverse()

for i in range(n,piv-1,-1):
    print(l1[i],l1[piv])
    if l1[i]>l1[piv]:
        l1[i],l1[piv]=l1[piv],l1[i]
        break

print(l1)

print()
print()

def rotate(matrix):
        l1=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j])
        return l1
      
matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
l2=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(matrix)
for i in l2:
    i.reverse()
print(l2)


#find subarrays
# def find_subarrays(arr):
#     subarrays = []
#     n = len(arr)
#     for start in range(n):
#         for end in range(start, n):
#             subarrays.append(arr[start:end+1])
    
    # return subarrays
    # for i in subarrays:
    #     if sum(i)==k:
    #         return len(i)
    # else:
    #     return -1

# arr = [48,99,37,4,-31]
# subarrays = find_subarrays(arr)
# subarrays.sort()
# print(subarrays)


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        l1 = []#(
        dict1 = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in dict1.values():
                l1.append(i)
            elif i in dict1:
                if not l1 or l1[-1] != dict1[i]:
                    return False
                l1.pop()
        return not l1
        
# chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
l1 = []
for i in chars:
    if i not in l1:
        l1.append(i)
        c = chars.count(i)
        l1.append(str(c))
            
print(l1)


def permutations(s):
    result = []
    s = list(s)
    def find_permutations(start):
        if start == len(s):
            result.append(''.join(s))  # Join the list into a string and store it
            return
        
        for i in range(start,len(s)):
            s[start], s[i] = s[i], s[start]
            print(s[start], s[i])
            find_permutations(start+1)
            s[start], s[i] = s[i], s[start]
    find_permutations(0)
    return result

# print(permutations("abc"))

# Given two strings s1 and s2, return true if s2 contains a 
# permutation
#  of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# class Solution(object):
#     def permutations(self,s):
#         result = []
#         s = list(s)
#         def find_permutations(start):
#             if start == len(s):
#                 result.append(''.join(s)) 
#                 return
            
#             for i in range(start,len(s)):
#                 s[start], s[i] = s[i], s[start]
#                 find_permutations(start+1)
#                 s[start], s[i] = s[i], s[start]
#         find_permutations(0)
#         return result

    # def checkInclusion(self, s1, s2):
    #     l1 = self.permutations(s1)
    #     for i in l1:
    #         if i in s2:
    #             return True
    #     else:
    #         return False
        
# a = Solution()
# print(a.permutations("abc"))

l1 = []
def permutations(string,i=0):
    if i==len(string):
        s = "".join(string)
        l1.append(s)

    for j in range(i,len(string)):
        word = [ch for ch in string]
        word[i],word[j]=word[j],word[i]
        permutations(word,i+1)
    return l1
print(permutations("abc"))


def containsNearbyDuplicate(nums, k):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    if i-j<=k:
                        return True
        return False
print(containsNearbyDuplicate([1,2,3,1],3))


# match = "Harshal"
# print(match)
# opt = int(input("Enter option :"))
# match opt:
#     case 1:
#         print("1")
#     case 2:
#         print("2")
#     case _:
#         print("_")


digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
mapping = {
    "1":[],
    "2":['a','b','c'],
    "3":['d','e','f'],
    "4":['g','h','i'],
    "5":['j','k','l'],
    "6":['m','n','o'],
    "7":['p','q','r','s'],
    "8":['t','u','v'],
    "9":['w','x','y','z']
}

def letterCombinations(digits):
    for i in digits:
        if i in mapping.keys():
            mapping[i]

letterCombinations(digits)

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
            # print(result)
        return result

a = Solution()
print(a.subsets([1,2,2]))


def count_substring(string, sub_string):
    c = 0
    for i in range(len(string)-len(sub_string)+1):
        print(string[i:len(sub_string)+i])
        if string[i:len(sub_string)+i]==sub_string:
            c+=1
    return c

print(count_substring("ABCDCDC","CDC"))

# def reverse(x: int) -> int:
#     res = 0
#     if x<0:
#         x = x*(-1)
#         while x>0:
#             r = x%10
#             res = (res*10)+r
#             x //= 10
#         return -res

# print(reverse(-1230))


class Solution:
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix

a = Solution()
print(a.transpose([[1,2,3],[4,5,6],[7,8,9]]))


def second_max(list1):
    s1 = set(list1)
    l1 = list(s1)
    l1.sort()
    if len(l1)==1:
        return None
    else:
        sm = l1[-2]
        return sm
print(second_max([2]))



def addSpaces( s, spaces) -> str:
    s1 = ''
    for i in range(len(s)):
        if i in spaces:
            s1 += ' '
        s1 = s1+s[i]
    return s1
print(addSpaces("LeetcodeHelpsMeLearn",[8,13,15]))


def getEncryptedString(s: str, k: int) -> str:
    s1 = ""*len(s)
    for i in range(len(s)):
        idx = (i+k)%len(s) 
        print(idx)
        s1 += s[idx]
    return s1

print(getEncryptedString("dart",3))
print()
print()

def countKeyChanges(s: str) -> int:
        c=0
        for i in range(len(s)-1):
            print(s[i],s[i+1])
            if s[i].lower()==s[i+1].lower():pass
            else:
                c+=1
        return c
print(countKeyChanges("aAbB"))
print()
print()
print()

def mul(a,b):
    if b == 0:
        return 0
    elif b>0:
        return a+mul(a,b-1)
    elif b<0:
        return -a+mul(a,b+1)

# print("Mul : ",mul(4,6))
# print("Mul : ",mul(4,-6))
# print("Mul : ",mul(-4,-6))


l1 = [2,3,4,5,6,7,8,9]
d1 = {i:l1[i] for i in range(len(l1))}
# print(d1)

def reverseInGroups(arr, k):
    l1 = arr[k-1::-1]+arr[-1:-k:-1]
    return l1

print(reverseInGroups([1,2,3,4,5],3))

from collections import deque
import re
def isMatch(s: str, p: str) -> bool:
        res = re.fullmatch(p,s)
        return True if res else False

print(isMatch(r"?a","ba"))

def rotate(arr):
        l1 = [0]*len(arr)
        l1[0] = arr[-1]
        for i in range(len(arr)-1):
            l1[i+1]=arr[i]
        return l1

print(rotate([1,2,3,4,5]))



n = 10
count = 0
for i in range(2,3):
    c = 0
    for J in range(1,i+1):
        if i%J==0:
            c+=1
    if c==2:
        count+=1
print(c)


def reverseArray(arr):
        # code here
        start = 0
        end = len(arr)-1
        while start<end:
            arr[end],arr[start]=arr[start],arr[end]
            start+=1
            end-=1
        return arr

print(reverseArray([1,2,3,4,5]))
print("====================================")
def searchMatrix(matrix, target: int) -> bool:
        for i in matrix:
            for j in i:
                print(i)
                if target in i:
                    return True
        return False

print(searchMatrix([[1,2],[4,5]],13))

print("=======================================")
def rotateArr(arr, d):
        #Your code here
        arr = arr[d:]+arr[:d]
        return arr
# arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]
print(rotateArr([1, 2, 3, 4, 5],2))
print("=======================================")


def isIsogram(s):
        #Your code here
        for i in s:
            if s.count(i)>1:
                return 0
        return 1

s = 'machine'
print(isIsogram(s))


def isIsogram(s):
        if len(set(s))==len(s):
            return 1
        return 0

s = 'machine'
print(isIsogram(s))

email = 'harshalkharabe4@gmail.com'
domain = 'gmil.com'
dn = len(email)-len(domain)
if domain==email[dn:]:
    print("Exist")
else:
    print("Not Exist")


#Find square root of number
num = 25
sqrt = num**0.5
print(sqrt)

email = "harshalkharabe4@gmail.com"
domain = 'com'
email_domain = email.split("@")[1]
print(email_domain)
if email_domain == domain:
    print("The domain matches!")


# Find Third largest number in list
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         max_1,max_2,max_3=0,0,0
#         nums.sort()
#         max_1 = nums[-1]
#         if nums.count(max_1)<len(nums):
#             max_2 = nums[-(nums.count(max_1))-1]
#         if (nums.count(max_1)+nums.count(max_2))<len(nums):
#             max_3 = nums[-(nums.count(max_1)+nums.count(max_2))-1]
#             return max_3
        # return max_1
    

def leftRotate(self, arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    arr[:] = arr[k:] + arr[:k]  # Modify in-place
    return arr  # Optional, if returning is needed


# Upper to Lower
s="harshal"
s1 = ""
for i in s:
    s1+=chr(ord(i)-32)
print("Upper :",s1)

#User input Upper to Lower
s=input("Enter your name : ")
s1 = ""
for i in s:
    if (i>="a" and i<="z"):
        s1+=chr(ord(i)-32)
    elif (i>="A" and i<="Z"):
        s1+=chr(ord(i)+32)
print("Upper :",s1)


# Find maximum sub-array sum.
def subarrsum(arr):
    max_sum = max_sum = float('-inf')
    current_sum=0
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum

print("Max sum : ",subarrsum([-2,1,-3,4,-1,2,1,-5,4]))


# Find maximum sub-array sum with sub-array.
def findmaxsubarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = end = temp_start = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return max_sum, arr[start:end + 1]

print("Max sum and sub-array : ",findmaxsubarray([-2,1,-3,4,-1,2,1,-5,4]))


lst = ['yyyy-mm-dd', 'yyyy/mm/dd', 'dd-mm-yyyy', 'dd/mm/yyyy', 'mm/dd/yyyy', 'mm-dd-yyyy', 'yyyy-dd-mm', 'yyyy/dd/mm']
f = 'yyyy-mm-dd'
if f not in lst:
    print("Not Exist")
else:
    print("Exist")


# Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k. The output should be an array of maximum values corresponding to each contiguous subarray.
def max_of_subarrays(arr, n, k):
    if not arr or k == 0:
        return []

    n = len(arr)
    result = []
    dq = deque()

    for i in range(n):
        # Remove elements that are out of this window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove all elements smaller than the current element (they won't be needed)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Add current element index to the deque
        dq.append(i)

        # Add maximum element of current window to result (from index k-1 onwards)
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1            
        right += 1
    return s[left + 1:right] 

def findLongestpalindrome(s):
    if not s:
        return ""

    longest = ""
    
    for i in range(len(s)):
        # Odd-length palindromes (center at i)
        palindrome1 = expand_around_center(s, i, i)
        # Even-length palindromes (center between i and i+1)
        palindrome2 = expand_around_center(s, i, i + 1)

        # Choose the longer palindrome
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

def find_subarray(s1,s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0  

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
    return max_length


print(str(bool(1)+float(10)/float(2)))
print((bool(1)+float(10)/float(2)))
# print(v)

a = ['a','b','c','d','e']
# Thrown memory run time error.
# for i in a:
#     a.append(i.upper()) 
# print(a)

def find_subarray(s1,s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
    return s1[end_index - max_length:end_index] if max_length > 0 else ""

print(find_subarray("abcdxyz","xyzabcd"))


from collections import Counter

def can_equalize_frequency(s: str) -> bool:
    freq = Counter(s)
    freq_count = Counter(freq.values())

    if len(freq_count) == 1:
        # All characters have same frequency
        return True

    if len(freq_count) == 2:
        (f1, c1), (f2, c2) = freq_count.items()

        # Ensure f1 < f2 for easier logic
        if f1 > f2:
            f1, f2 = f2, f1
            c1, c2 = c2, c1

        # Case 1: One character occurs once and its frequency is 1
        if f1 == 1 and c1 == 1:
            return True

        # Case 2: Frequencies differ by 1 and the higher one occurs only once
        if f2 == f1 + 1 and c2 == 1:
            return True

    return False



def digital_root(n):
    # ...
    s=0
    while True:
        s = 0
        while n>0:
            r = n%10
            s=s+r
            n//=10
        if s>9:
            n=s
        else:break
    return s

print(f"Sum of digit : {digital_root(942)}")
print(f"Sum of digit : {digital_root(19)}")
print(f"Sum of digit : {digital_root(92)}")


def removeReverse(S):
    from collections import Counter

    freq = Counter(S)
    s = list(S)
    left, right = 0, len(s) - 1
    direction = True  # True means left to right, False means right to left

    while True:
        found = False

        if direction:
            # Check from left to right
            while left <= right:
                if freq[s[left]] > 1:
                    freq[s[left]] -= 1
                    s.pop(left)
                    right -= 1  # since we removed one from left
                    found = True
                    direction = not direction
                    break
                else:
                    left += 1
        else:
            # Check from right to left
            while right >= left:
                if freq[s[right]] > 1:
                    freq[s[right]] -= 1
                    s.pop(right)
                    right -= 1
                    found = True
                    direction = not direction
                    break
                else:
                    right -= 1

        if not found:
            break

    return ''.join(s)


def firstElementKTime(arr,k):
        d1 = {}
        for num in arr:
            d1[num] = d1.get(num, 0) + 1
            if d1[num] == k:
                return num
        return -1

firstElementKTime([12,12,1,322,32,4354],3)


def find_rotation_count(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) // 2
        next_ = (mid + 1) % len(arr)
        prev = (mid - 1 + len(arr)) % len(arr)

        if arr[mid] <= arr[prev] and arr[mid] <= arr[next_]:
            return mid

        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1

    return 0

print(find_rotation_count([3,4,5,1,2]))

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Fill the DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

seen = set()
result = []

def remove_duplicates(s):
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
        return ''.join(result)

def roman_to_int(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(s):
        curr_value = roman_map[char]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
            prev_value = curr_value
    return total

from collections import Counter

class Solution:
    def findMajority(self, arr):
        n = len(arr) // 3
        count = Counter(arr)  # O(n)
        result = [num for num, freq in count.items() if freq > n]
        return sorted(result)

def duplicates(s):
    if not s:
        return ""
    
    result = [s[0]]
    
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result.append(s[i])
    
    return ''.join(result)
print(duplicates("aaabbbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"))


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]


# Function to find maximum
# product subarray
def maxProduct(arr):
    # code here
    if not arr:
        return 0
    max_product = arr[0]
    min_product = arr[0]       
    result = arr[0]       
    for i in range(1,len(arr)):
        num = arr[i]
        temp_max = max(num,num*max_product,num*min_product)
        min_product = min(num,num*max_product,num*min_product)
        max_product = temp_max
        result = max(result,max_product)
    return result


print(maxProduct([2, 3, -2, 4])) #output : 6
print(maxProduct([2, 3, -2, 4])) #output : 6

# min cost to climb stairs at top.
def climbing_steps(cost):
    n = len(cost)
    ele1 = cost[0]
    ele2 = cost[1]

    for i in range(2,n):
        curr = cost[i]+min(ele1,ele2)
        ele1=ele2
        ele2=curr
    return min(ele1,ele2)

print(climbing_steps([10,15,20]))

# stock buy and sell max profit.
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price<min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(profit,max_profit)
    return max_profit

print("Max profit :",max_profit([1,2,3,4,5,6])) # output : 5

class Solution:
    def compress(self, chars) -> int:
        write = 0
        read = 0

        while read < len(chars):
            current_char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            chars[write] = current_char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
s1 = Solution()
print(s1.compress("dsklcjdnojdnfamdk".split()))


class Solution:
    def circularSubarraySum(self, arr):
    # code here
        n = len(arr)
        res = arr[0]
        for i in range(n):
            currsum=0
            for j in range(n):
                idx = (i+j)%n
                currsum += arr[idx]
                res = max(res,currsum)
        return res
s2 = Solution()
subarr1 = s2.circularSubarraySum([5, -2, 3, 4, -1, 2, -3, 6]) # Output: 15
print(f"Subarray sum : {subarr1}")

def fun(arr):
    start = 0
    end = n - 1
    while start < end:
        if arr[start] > arr[end]:
            start += 1
        else:
            end -= 1
    return arr[start]

def pivotIndex(nums) -> int:
    for i in range(len(nums)):
        if (sum(nums[:i])+0)==(0+sum(nums[i+1:])):
            return i
    return -1

def groupAnagrams(strs):
    l1=[]
    for i in range(len(strs)):
        l2=[]
        for j in range(len(strs)):
            if strs[i] in strs[j]:
                l2.append(strs[j])
        l1.append(l1)
    return l1

res = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(res)

class Solution:
    def findMaxAverage(self, nums):
        s = sum(nums[:k])
        m = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            if s > m:
                m = s
        return m / float(k)
    
    def groupAnagrams(self, strs):
        dict1 = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dict1:
                dict1[sorted_word] = []
            dict1[sorted_word].append(word)
        return list(dict1.values())

    def longestSubarray(self, nums):
        n = len(nums)

        left = 0
        zeros = 0
        ans = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == n else ans
arr = [20,33,4,3253235,235,245,5,325]
x = 235
def find(arr):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
print(f"Result : {find(arr)}")

def binarysearch(arr,x):
    arr.sort()
    lb = 0
    ub = len(arr) - 1
    mid = len(arr) // 2
    while lb <= ub:
        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
            lb = mid + 1
        elif arr[mid]>x:
            ub = mid - 1
        mid = (lb + ub) // 2
        return mid
    return -1
arr = [1,3232,4,354,325,325,325,5,35,5,9]
x = 9
print(f"Middle index : {binarysearch(arr,x)}")



from collections import Counter
def closeStrings(self, word1: str, word2: str) -> bool:
    if len(word1)!=len(word2):
        return False
    if set(word1) == set(word2):
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return True if sorted(cnt1.values()) == sorted(cnt2.values()) else False
    return False


def removeStars(s: str) -> str:
    stack = []
    for char in s:
        if char == '*':
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

def find_maxsum_subarray(arr):
    max_sum = currentsum = arr[0]
    for num in arr[1:]:
        currentsum = max(num, currentsum + num)
        max_sum = max(max_sum, currentsum)
    return max_sum

def maxproduct_subarray(arr):
    # arr = [2, 3, -2, 4]
    max_product = min_product = result = arr[0]
    for num in arr[1:]:
        choices = (num,num*max_product,num*min_product)
        max_product = max(choices)
        min_product = min(choices)
        result = max(result,max_product)
    return result
# o/p = 6