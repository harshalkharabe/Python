# 1.Given an array arr of integers, check if there exist two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 
# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Example 2:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

# Solution :
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         l1 = arr
#         for i in range(len(l1)):
#             for j in range(len(l1)):
#                 if i!=j and l1[j]*2==l1[i]:
#                     return True
#         return False

# 2.Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

# Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.
# A prefix of a string s is any leading contiguous substring of s.

# Example 1:
# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

# Example 2:
# Input: sentence = "this problem is an easy problem", searchWord = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.

# Solution :
# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         idx = -1
#         l1 = sentence.split(' ')
#         for i in range(len(l1)):
#             if l1[i].startswith(searchWord):
#                 idx = i+1
#                 return idx
#         return idx

# 3.You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.

# Example 1:
# Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
# Output: "Leetcode Helps Me Learn"
# Explanation: 
# The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
# We then place spaces before those characters.

# Solution :
# class Solution:
#     def addSpaces(self, s: str, spaces: List[int]) -> str:
#         spaces = set(spaces)
#         s1 = ''

#         for i in range(len(s)):
#             if i in spaces:
#                 s1 += ' '
#             s1 = s1+s[i]
#         return s1

# 4.You are given two 0-indexed strings str1 and str2.
# In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.
# Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.
# Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

# Example 1:
# Input: str1 = "abc", str2 = "ad"
# Output: true
# Explanation: Select index 2 in str1.
# Increment str1[2] to become 'd'. 
# Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.

# Solution (chatgpt)
# class Solution:
#     def canMakeSubsequence(self, str1: str, str2: str) -> bool:
#         i,j=0,0
#         n,m=len(str1),len(str2)
#         while i<n and j<m:
#             if str1[i]==str2[j] or (ord(str1[i]) + 1 - ord('a')) % 26 == ord(str2[j]) - ord('a'):               j+=1
#             i+=1
#         return j==m


# 5.You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:
# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

# Example 1:
# Input: start = "_L__R__R_", target = "L______RR"
# Output: true
# Explanation: We can obtain the string target from start by doing the following moves:
# - Move the first piece one step to the left, start becomes equal to "L___R__R_".
# - Move the last piece one step to the right, start becomes equal to "L___R___R".
# - Move the second piece three steps to the right, start becomes equal to "L______RR".
# Since it is possible to get the string target from start, we return true.
# Example 2:
# Input: start = "R_L_", target = "__LR"
# Output: false
# Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
# After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
# Example 3:
# Input: start = "_R", target = "R_"
# Output: false
# Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.

# Solution (chatgpt)
# class Solution:
#     def canChange(self, start: str, target: str) -> bool:
#         if start.replace("_", "") != target.replace("_", ""):
#             return False
#         i, j = 0, 0
#         n = len(start)
#         while i < n and j < n:
#             while i < n and start[i] == '_':
#                 i += 1
#             while j < n and target[j] == '_':
#                 j += 1
#             if i == n and j == n:
#                 return True
            
#             if i == n or j == n:
#                 return False
#             if start[i] != target[j]:
#                 return False
#             if start[i] == 'L' and i < j:
#                 return False
#             if start[i] == 'R' and i > j:
#                 return False
#             i += 1
#             j += 1
        
#         return True

# 6.You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:
# The chosen integers have to be in the range [1, n].
# Each integer can be chosen at most once.
# The chosen integers should not be in the array banned.
# The sum of the chosen integers should not exceed maxSum.
# Return the maximum number of integers you can choose following the mentioned rules.

# Example 1:
# Input: banned = [1,6,5], n = 5, maxSum = 6
# Output: 2
# Explanation: You can choose the integers 2 and 4.
# 2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.
# Example 2:
# Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
# Output: 0
# Explanation: You cannot choose any integer while following the mentioned conditions.

# Solution 
# class Solution:
#     def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
#         banned_set = set(banned)
#         l1 = [i for i in range(1,n+1) if i not in banned_set]
#         l1.sort()

#         total = 0
#         count = 0
#         for num in l1:
#             if total+num <= maxSum:
#                 total += num
#                 count+=1
#         return count

# 7.You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.
# You can perform the following operation at most maxOperations times:
# Take any bag of balls and divide it into two new bags with a positive number of balls.
# For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
# Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.
# Return the minimum possible penalty after performing the operations.

# Example 1:
# Input: nums = [9], maxOperations = 2
# Output: 3
# Explanation: 
# - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
# - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
# The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

# Solution (chatgpt)
# class Solution:
#     def minimumSize(self, nums: List[int], maxOperations: int) -> int:
#         def canAchieveMaxBagSize(maxSize):
#             operations_needed = 0
#             for balls in nums:
#                 # If balls <= maxSize, no splits are needed
#                 if balls > maxSize:
#                     # Calculate the number of splits required
#                     operations_needed += math.ceil(balls / maxSize) - 1
#                 if operations_needed > maxOperations:
#                     return False
#             return operations_needed <= maxOperations

#         # Binary search for the minimum possible penalty (maximum bag size)
#         left, right = 1, max(nums)
#         while left < right:
#             mid = (left + right) // 2
#             if canAchieveMaxBagSize(mid):
#                 right = mid  # Try for a smaller maximum bag size
#             else:
#                 left = mid + 1  # Increase the maximum bag size
        
#         return left   


def peakElement(arr):
        # Code here
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                return True
        return False

print(peakElement([1,2,3]))