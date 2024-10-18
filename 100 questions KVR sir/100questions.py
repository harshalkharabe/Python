# # 1. Write a Python program to sum all the items in a list.

l1 = [1,3,6,8,3,5,7,99]
print(f"Sum : {sum(l1)}")

# # 2. Write a Python program to multiply all the items in a list. 
l1 = [1,3,6,8,3,5,7,99]
p = 1
for i in l1:
    p *= i
print(f"Multiplication : {p}")

# # 3. Write a Python program to get the largest number from a list. 
l1 = [1,3,6,8,3,5,7,99]
print(f"Maximum : {max(l1)}")

# # 4. Write a Python program to get the smallest number from a list.
l1 = [1,3,6,8,3,5,7,99]
print(f"Minimum : {min(l1)}")

# # 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# # 		Sample List : ['abc', 'xyz', 'aba', '1221']
# # 		Expected Result : 2

l1 = ['abc', 'xyz', 'aba', '1221']
for i in range(len(l1)):
    if l1[i][0]==l1[i][-1]:
        if l1[i].isalpha():
            idx = i

print(f"String : {l1[idx]} Index : {idx}")

# # 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# # 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i][-1]>l1[j][-1]:
            l1[i],l1[j]=l1[j],l1[i]
print("Sorted listed : ",l1)

# 7. Write a Python program to remove duplicates from a list.
l1 = [12,45,12,56,78,33]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(f"Original list : {l1}")
print(f"After removing duplicates : {l2}")

# # 8. Write a Python program to check a list is empty or not.

l1 = [12]
res = "Non-Empty list" if len(l1)>0 else "Empty"
print(res)

# # 9. Write a Python program to clone or copy a list.

l1 = [12,45,32,21,78,56]
l2 = []
for i in l1:
    l2.append(i)
print(f"After copy list : {l2}")

# # 10. Write a Python program to find the list of words that are longer than n from a given list of words.


# #====================Remove given element from list===============================
list1=[10,20,30,10,10,20,40,50,60,10,10,90,80]
value=10
print(list1)

while True:
    if value in list1:
        list1.remove(10)
    else:
        break
print(list1)

# #========================================================================
# # 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def checkCommonMember(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
    else:
        return False

l1 = [12,34,5,678,90]
l2 = [12,31,50,67,9]
print(f"Lists contain common elements : {checkCommonMember(l1,l2)}")


# # 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# # 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # 		Expected Output : ['Green', 'White', 'Black']

l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(l1)
# value = '_'
# while True:
#     for i in range(len(l1)):
#         if i==0 or i==4 or i==5:
#             l1.remove(l1[i])
#             l1.insert(i,"_")
#             print("hjhjk")
#     else:
#         break
# while True:
#     if value in l1:
#         l1.remove(value)
#     else:
#         break

for i in range(len(l1)-1,-1,-1):
    if i==5 or i==4 or i==0:
        del l1[i]

print(l1)


# # 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 




# # 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 

l1 = list(range(1,51))
for i in range(len(l1)-1,-1,-1):
    if l1[i]%2==0:
        del l1[i]
print(l1)

# # 15. Write a Python program to shuffle and print a specified list.

