#Find the Second Largest Number in a List
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
