# # # 1. Write a Python program to sum all the items in a list.

# l1 = [1,3,6,8,3,5,7,99]
# print(f"Sum : {sum(l1)}")

# # # 2. Write a Python program to multiply all the items in a list. 
# l1 = [1,3,6,8,3,5,7,99]
# p = 1
# for i in l1:
#     p *= i
# print(f"Multiplication : {p}")

# # # 3. Write a Python program to get the largest number from a list. 
# l1 = [1,3,6,8,3,5,7,99]
# print(f"Maximum : {max(l1)}")

# # # 4. Write a Python program to get the smallest number from a list.
# l1 = [1,3,6,8,3,5,7,99]
# print(f"Minimum : {min(l1)}")

# # # 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# # # 		Sample List : ['abc', 'xyz', 'aba', '1221']
# # # 		Expected Result : 2

# l1 = ['abc', 'xyz', 'aba', '1221']
# for i in range(len(l1)):
#     if l1[i][0]==l1[i][-1]:
#         if l1[i].isalpha():
#             idx = i

# print(f"String : {l1[idx]} Index : {idx}")

# # # 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# # # 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # # 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i][-1]>l1[j][-1]:
#             l1[i],l1[j]=l1[j],l1[i]
# print("Sorted listed : ",l1)

# # 7. Write a Python program to remove duplicates from a list.
# l1 = [12,45,12,56,78,33]
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(f"Original list : {l1}")
# print(f"After removing duplicates : {l2}")

# # # 8. Write a Python program to check a list is empty or not.

# l1 = [12]
# res = "Non-Empty list" if len(l1)>0 else "Empty"
# print(res)

# # # 9. Write a Python program to clone or copy a list.

# l1 = [12,45,32,21,78,56]
# l2 = []
# for i in l1:
#     l2.append(i)
# print(f"After copy list : {l2}")

# # # 10. Write a Python program to find the list of words that are longer than n from a given list of words.
l1 = ['Harshal','Sagar','Kunal',"Ram",'Ankush','paa','pukii']
l = int(input("Enter lenght : "))
for i in l1:
    if len(i)>=l:
        print(i)

# # #====================Remove given element from list===============================
# list1=[10,20,30,10,10,20,40,50,60,10,10,90,80]
# value=10
# print(list1)

# while True:
#     if value in list1:
#         list1.remove(10)
#     else:
#         break
# print(list1)

# # #========================================================================
# # # 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# def checkCommonMember(l1,l2):
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 return True
#     else:
#         return False

# l1 = [12,34,5,678,90]
# l2 = [12,31,50,67,9]
# print(f"Lists contain common elements : {checkCommonMember(l1,l2)}")


# # # 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# # # 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # # 		Expected Output : ['Green', 'White', 'Black']

# l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(l1)
# # value = '_'
# # while True:
# #     for i in range(len(l1)):
# #         if i==0 or i==4 or i==5:
# #             l1.remove(l1[i])
# #             l1.insert(i,"_")
# #             print("hjhjk")
# #     else:
# #         break
# # while True:
# #     if value in l1:
# #         l1.remove(value)
# #     else:
# #         break

# for i in range(len(l1)-1,-1,-1):
#     if i==5 or i==4 or i==0:
#         del l1[i]

# print(l1)


# # # 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 




# # # 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 

# l1 = list(range(1,51))
# for i in range(len(l1)-1,-1,-1):
#     if l1[i]%2==0:
#         del l1[i]
# print(l1)

# # # 15. Write a Python program to shuffle and print a specified list.
# l1 = [12,3,45,66,789,0]
# l1.sort()
# print(l1)

# #========================================================================
# # 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 

# l1 = list(range(1,31))
# for i in l1:
#     if i<=5 or i>=25:
#         print(f"{i} --> {i*i}")

# # 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 

# l1 = list(range(1,31))
# s1 = list([i*i for i in range(1,31)])
# # for i in range(5):
# #     val = int(input("Enter value : "))
# #     if val in l1 or val in s1:
# #         print(f"Present in list")
# #     else:
# #         print("Not present")

# # 18. Write a Python program to generate all permutations of a list in Python.



# # 19. Write a Python program to get the difference between the two lists. 

# l1 = [1,2,3,4,5,6,7,8,9,]
# l2 = [11,12,8,9,10]
# l3 =[]
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print(l1,l2,l3,sep='\n')

# # 20. Write a Python program access the index of a list.
# l1 = list(range(1,11))
# for i in range(len(l1)):
#     print(i,end=' ')


# # 21. Write a Python program to convert a list of characters into a string. 

# l1 = ['H','a','r','s','h','a','l']
# s = ''
# for i in l1:
#     s += i
# print(f"After Converting list :{l1} into string : {s}")

# # 22. Write a Python program to find the index of an item in a specified list. 
l1 = [12,34,56,78,34,34,89]
n = int(input("Enter number : "))
idx=-1
for i in range(len(l1)):
    if l1[i]==n:
        idx=i
print(f"Index of given value in list is {idx}")



# # 23. Write a Python program to flatten a shallow list. 

# l1 = [[22,33,44],[12,34,56,9],[1,2,3,4,5,6]]
# l2 = []

# for i in l1:
#     for j in i:
#         l2.append(j)
# l2.sort()
# print("Flatten : ",l2)

# # 24. Write a Python program to append a list to the second list. 

# l1 = [1,2,3,4,5,6,7,8,9,10,]
# l2 = []
# for i in l1:
#     l2 = l2 + [i]
# print("After appending 1st list into 2nd : ",l2)

# # 25. Write a Python program to select an item randomly from a list. 
# import random
# list1 = ["Harshal","Sagar","Aniket","Prathamesh","Kunal"]
# l1 = random.choice(list1)
# print(l1)

# # 26. Write a python program to check whether two lists are circularly identical.



# # 27. Write a Python program to find the second smallest number in a list. 

# l1 = [12,34,56,78,9,2,2,2]
# m = min(l1)
# c = l1.count(m)
# l1.sort()
# print(f"Second Smallest : {l1[c]}")

# #=================SECOND WAY=========================
# l1 = [12,34,56,78,9,2,2,2]
# min = l1[0]
# smin = l1[0]
# for i in l1:
#     if i<min:
#         smin=min
#         min = i
#     if i<smin<min:
#         smin=i
    
# print(f"Min : {min} Second Min : {smin}")
    

# # 28. Write a Python program to find the second largest number in a list. 

# l1 = [12,34,5,21,45,76,21,76]
# m = max(l1)
# c = l1.count(m)
# l1.sort()
# print(f"Second Maximum : {l1[-(c+1)]}")

# l2 = [12,34,5,21,45,76,21,76]
# m = 0
# smax = 0
# for i in l2:
#     if i>m:
#         smax=m
#         m = i
#     if m>i>smax:
#         smax=i
# print(f"Max {m} Second Max : {smax}")

# # 29. Write a Python program to get unique values from a list. 

# l1 = [12,34,4,56,78,56,65,5,4,56,64,67,12,543,4]
# print("unique values : ",end=' ')
# for i in l1:
#     if l1.count(i)==1:
#         print(i,end=' ')

# # 30. Write a Python program to get the frequency of the elements in a list.
# print()
# l1 = [12,34,4,56,78,56,65,5,4,56,64,67,12,543,4]
# dict1 = {}
# for i in l1:
#     dict1[i] = l1.count(i)
# print("Frequency of the elements : ",dict1)

# #==============================================================================
# # 31. Write a Python program to count the number of elements in a list within a specified range.
# l1 = [12,3,54,22,17,20,14,4,6,7,9,8]
# for i in range(3,21):
#     if i in l1:
#         print(i,end=' ')

# #=================================================================================
# # 32. Write a Python program to check whether a list contains a sublist.
# print()
# l1 = [1,2,3,4,5,6,7]
# l2 = [4,5,6,7]
# l=len(l2)
# for i in range(len(l1)-len(l2)+1):
#     if l1[i:i+l]==l2:
#         print(f"{l2} is sublist of {l1}")
#         break
# else:
#     print(f"{l2} is not sublist of {l1}")


# #=================================================================================
# # 33. Write a Python program to generate all sublists of a list. 


# #=================================================================================
# # 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# # 	Sample list : ['p', 'q']
# # 	n =5
# # 	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# # s1 = ['p','q']
# # n=5
# # s2 = []
# # for i in range(n):
# #     s2.append(s1[0]+str(i+1))
# #     s2.append(s1[1]+str(i+1))
# # print(s2)

# #=================================================================================
# # 36. Write a Python program to get variable unique identification number or string. 

# #=================================================================================
# # 37. Write a Python program to find common items from two lists.
# # l1 = [3,4,5,6,7,8]
# # l2 = [1,2,3,4,5,8]
# # l3 = []
# # for i in l1:
# #     if i in l2:
# #         l3.append(i)
# # print(l3)

# #=================================================================================
# # 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
# # 	Sample list: [0,1,2,3,4,5]
# # 	Expected Output: [1, 0, 3, 2, 5, 4]

# # l1 = [0,1,2,3,4,5]
# # i=0
# # while i<len(l1)-1:
# #     l1[i],l1[i+1]=l1[i+1],l1[i]
# #     i+=2
# # print(l1)
# #=================================================================================
# # 39. Write a Python program to convert a list of multiple integers into a single integer. 
# # 		Sample list: [11, 33, 50]
# # 		Expected Output: 113350

# # l1 = [11,32,50]
# # digit = 0
# # for num in l1:
# #     num1=num
# #     c = 0
# #     while num>0:
# #         c+=1
# #         num//=10
# #     print(c)
# #     digit = (digit*(10**c))+num1
# #     print(digit)
# # print(digit)
    
# #=================================================================================
# # 40. Write a Python program to split a list based on first character of word.      
# # words = ["apple", "banana", "apricot", "berry", "cherry", "carrot","pappya"]
# # dict1 = {}
# # i=0
# # while i<len(words):
# #     ch = words[i][0]
# #     dict1[ch]=list()
# #     for word in words:
# #         if ch == word[0]:
# #             dict1[ch].append(word)
# #     i+=1
# # print(dict1)

# # 41. Write a Python program to create multiple lists.      
# l1 = list()
# print(f"Empty list : {l1}")
# l2 = [12,34,56,9]
# print(f"List : {l2}")
# l3 = [i for i in range(1,11)]
# print(f"List : {l3}")

# # 42. Write a Python program to find missing and additional values in two lists.      
# # 	Sample data : Missing values in second list: b,a,c
# # 	Additional values in second list: g,h

l1 = [12,34,56,78,54,3]
l2 = [34,56,7,12]
missing_values = []
additional_values = []
for i in l1:
    if i not in l2:
        missing_values.append(i)
for i in l2:
    if i not in l1:
        additional_values.append(i)
    
print("Missing values in second list : ",missing_values)
print("Additional values in l2 : ",additional_values)

# # 43. Write a Python program to split a list into different variables. 
a,b,c=[12,34,56]
print("After spliting list intop three variables : ",a,b,c)
a,b,*c=[12,34,56,43,21,23]
print("After spliting list intop three variables : ",a,b,c)

# # 44. Write a Python program to generate groups of five consecutive numbers in a list. 
# l1 = [[int(input("Values : ")) for i in range(3)] for val in range(2)]
# print(l1)

# # 45. Write a Python program to convert a pair of values into a sorted unique array.
a=int(input("Enter number : "))
b=int(input("Enter number : "))
if a==b:
    l1 = [a]
else :
    l1 = [a]+[b]
print(l1)

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



# 51. Write a Python program to split a list every Nth element. 
# 	Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# 	Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]



# 52. Write a Python program to compute the difference between two lists.      
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# 	Color1-Color2: ['white', 'orange', 'red']
# 	Color2-Color1: ['black', 'yellow']
l1 = ["red", "orange", "green", "blue", "white"]
l2 = ["black", "yellow", "green", "blue"]

print("Color1-Color2")
for i in l2:
    if i not in l1:
        print(i)

print("Color2-Color1")
for i in l1:
    if i not in l2:
        print(i)

# 53. Write a Python program to create a list with infinite elements.
# n=0
# i=0
# l1=[]
# while True:
#     n+=1
#     l1.append(n)
#     print(l1)

# 54. Write a Python program to concatenate elements of a list.

l1 = ["My","Name","is","Harshal","Kharabe"]
s1 = ''
for i in l1:
    s1 = s1+i+" "
print(s1)

# 55. Write a Python program to remove key values pairs from a list of dictionaries.

# 56. Write a Python program to convert a string to a list. 
s = "Harshal"
l1 = [ch for ch in s]
print("String to List :",l1)

# 57. Write a Python program to check if all items of a given list of strings is equal to a given string.
def check(l1,s) :
    for i in l1:
        if i != s:
            return False
    return True
l1 = ["Harshal","Kharabe"]
s = "Harshal"
print(f"Check {s} is equal to all words in list or not : ",check(l1,s))

# 58. Write a Python program to replace the last element in a list with another list. 
# 	Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# 	Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]
l3 = []
for i in range(len(l1)-1):
    l3.append(l1[i])
for i in range(len(l2)):
    l3.append(l2[i])
print(l3)
# 59. Write a Python program to check whether the n-th element exists in a given list. 
l1 = [12,34,32,56,54,78,9,10]
nth_ele = int(input("Enter nth element position : "))
if nth_ele<len(l1):
    print("Exist")
else:
    print("Not Exist")

# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
l1 = [(2,4),(2,3),(5,1),(4,3),(2,4)]
stup = l1[0][-1]
print(stup)
smallest=None
for i in range(len(l1)):
        if stup>l1[i][-1]:
            stup = l1[i][-1]
            smallest=l1[i]
print("Smallest second tuple value : ",smallest)

# 61. Write a Python program to create a list of empty dictionaries. 

l1 = [dict() for i in range(5)]
print(l1)
# 62. Write a Python program to print a list of space-separated elements.

# 63. Write a Python program to insert a given string at the beginning of all items in a list.
# 	Sample list : [1,2,3,4], string : emp
# 	Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
l1 = [1,2,3,4]
l2 = []
s = "emp"
for i in l1:
    s1 = s+str(i)
    l2.append(s1)
print(l2)

# 64. Write a Python program to iterate over two lists simultaneously.
l1 = [12,34,56,78,89]
l2 = [1,3,6,8,9]
for i in range(len(l1)):
    print(l1[i],l2[i])
# 65. Write a Python program to move all zero digits to end of a given list of numbers. 
# 	Expected output:
# 	Original list:
# 	[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# 	Move all zero digits to end of the said list of numbers:
# 	[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

l1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
for j in range(len(l1)):
    for i in range(len(l1)-1):
        if l1[i]==0:
            l1[i+1],l1[i]=l1[i],l1[i+1]
print(l1)

# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. 
# 	Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# 	Expected Output: [10, 11, 12]
l1 = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
s = 0
for i in l1:
    if sum(i)>s:
        s=sum(i)
        l2 = i
print(l2)
# 67. Write a Python program to find all the values in a list are greater than a specified number. 
l1 = [1,2,3,4,5,6,7,89,34,4,35,54,56,56,7,6]
num = 6
print(f'All elements in list greater than {num} :')
for i in l1:
    if i>num:
        print(i,end=' ')
print()
# 68. Write a Python program to extend a list without append.      
# 	Sample data: [10, 20, 30]
# 	[40, 50, 60]
# 	Expected output : [40, 50, 60, 10, 20, 30]
l1 = [10,20,30]
l2 = [40,50,60]
l2[len(l2):len(l2)]=l1
print(l2)
# 69. Write a Python program to remove duplicates from a list of lists.      
# 		Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# 		New List : [[10, 20], [30, 56, 25], [33], [40]]

l1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print("After Removing Duplicate : ",l2)

# 70. Write a Python program to find the items starts with specific character from a given list. 
# 		Expected Output:
# 		Original list:
# 		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# 		Items start with a from the said list:
# 		['abcd', 'abc', 'acjd']
# 		Items start with d from the said list:
# 		['dagfa']
# 		Items start with w from the said list:
# 		[]

# 71. Write a Python program to check whether all dictionaries in a list are empty or not. 
# 	Sample list : [{},{},{}]
# 	Return value : True
# 	Sample list : [{1,2},{},{}]
# 	Return value : False

l1 = [{1},{},{}]
for i in l1:
    if len(i)>0:
        val = False
        break
    val = True
print(val)

# 72. Write a Python program to flatten a given nested list structure.
# 		Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# 		Flatten list:
# 		[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

l1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l2 = []
for i in l1:
    if type(i)==int or type(i)==float:
        l2.append(i)
    else:
        for j in i:
            l2.append(j)
print("Flattern list : ",l2)

# 73. Write a Python program to remove consecutive duplicates of a given list. 
# 		Original list:
# 		[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 		After removing consecutive duplicates:
# 		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

l1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l1.sort()
for i in range(len(l1)-1):
    if l1[i]==l1[i+1]:
        l1.remove(l1[i])
        l1.insert(i,'_')
print(l1)
l2=[]
for i in l1:
    if type(i)!=int:
        pass
    else:
        l2.append(i)
print(l2)

# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
# 	Original list:
# 	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 	After packing consecutive duplicates of the said list elements into sublists:
# 	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

l1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l2 = list(set(l1))
l3=[]
for i in l2:
    l4=[]
    c = l1.count(i)
    for j in range(c):
        l4.append(i)
    l3.append(l4)
print(l3)

# 75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4.3, 5, 1]
# 	List reflecting the run-length encoding from the said list:
# 	[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# 	Original String:
# 	automatically
# 	List reflecting the run-length encoding from the said string:
# 	[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]



# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	List reflecting the modified run-length encoding from the said list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Original String:
# 	aabcddddadnss
# 	List reflecting the modified run-length encoding from the said string:
# 	[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

# 77. Write a Python program to decode a run-length encoded given list.
# 	Original encoded list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Decode a run-length encoded said list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]

# 78. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Length of the first part of the list: 3
# 	Splited the said list into two parts:
# 	([1, 1, 2], [3, 4, 4, 5, 1])

l1 = [1, 1, 2, 3, 4, 4, 5, 1]
split_index = 3
l2 = []
for i in range(split_index):
    l2.append(l1[i])
l1 = l1[split_index:]
print(f"List After spliting : {l2,l1}")

# 79. Write a Python program to remove the K'th element from a given list, print the new list. Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	After removing an element at the kth position of the said list:
# 	[1, 1, 3, 4, 4, 5, 1]

l1 = [1, 1, 2, 3, 4, 4, 5, 1]
nth_index = 4
l2=[]
print(f"List before removing : {l1}")
for i in range(len(l1)):
    if i==nth_index:
        pass
    else:
        l2.append(l1[i])
print(f"List after removing nth index : {l2}")

# 80. Write a Python program to insert an element at a specified position into a given list. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	After inserting an element at kth position in the said list:
# 	[1, 1, 12, 2, 3, 4, 4, 5, 1]

l1=[1, 1, 2, 3, 4, 4, 5, 1]
ele = 45
kth_position = 3
l2 = l1[:kth_position]+[ele]+l1[kth_position:]
print("After inserting element at kth index : ",l2)

# 81. Write a Python program to extract a given number of randomly selected elements from a given list. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Selected 3 random numbers of the above list:
# 	[4, 4, 1]



# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. 
# HINT
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]



# 83. Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list. 
# 	Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# 	Result:
# 	243
l1 = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
l2 = [round(num) for num in l1]
print(l2)
result = sum(l2)*len(l2)
print("Sum after multiplying length of list :",result)
# 84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space. 
# 	Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# 	Minimum value: 4
# 	Maximum value: 22
# 	Result:
# 	20 25 45 55 60 70 80 90 110

l1 = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
l2 = [round(i) for i in l1]
l2.sort()
print(f"Minimum element : {min(l2)}")
print(f"Maximun element : {max(l2)}")
print("Result : ",end='')
for i in l2:
    print(i*5,end=' ')
print()

# 85. Write a Python program to create a multidimensional list (lists of lists) with zeros. 
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

l1 = [[0 for i in range(2)] for i in range(3)]
print("multi dimensional list of zeros :",l1)

# 86. Write a Python program to create a 3X3 grid with numbers.
# 	3X3 grid with numbers:
# 	[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# r = 3
# c = 3
# l1 = [[int(input("Enter val :")) for j in range(c)] for i in range(r)]
# print(l1)
# 87. Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user. 
# 	Input rows: 2
# 	Input columns: 2
# 	Input number of elements in a row (1, 2, 3):
# 	1 2
# 	3 4
# 	sum for each column:
# 	4 6

# r = 3
# c = 2
# l1 = [[int(input("Enter val :")) for j in range(c)] for i in range(r)]
# print(l1)
# s1,s2=0,0
# for c1,c2 in l1:
#     print(c1,c2)
#     s1+=c1
#     s2+=c2
# print("Sum : ",s1,s2)

# 88. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user. 
# 	Input the size of the matrix: 3
# 	2 3 4
# 	4 5 6
# 	3 4 7
# 	Sum of matrix primary diagonal:
# 	14
# r = 3
# c = 3
# s = 0
# l1 = [[int(input("Enter num : ")) for j in range(c)] for i in range(r)]
# print(l1)
# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if i==j:
#             s = s + l1[i][j]
# print(f'Sum of diagonal elements : {s}')

# 89. Write a Python program to Zip two given lists of lists. 
# 	Original lists:
# 	[[1, 3], [5, 7], [9, 11]]
# 	[[2, 4], [6, 8], [10, 12, 14]]
# 	Zipped list:
# 	[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]

l1 = [[1, 3], [5, 7], [9, 11]]
l2 = [[2, 4], [6, 8], [10, 12, 14]]
l3 = []
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
print("Zip list :",l3)

# 90. Write a Python program to count number of lists in a given list of lists. 
# 		Original list:
# 		[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 		Number of lists in said list of lists:
# 		4
# 		Original list:
# 		[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# 		Number of lists in said list of lists:
# 		3
# l2 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
l1 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
c = 0
for i in l2:
    if type(i)==list:
        c+=1
print("Total no.of.list :",c)

# 91. Write a Python program to find the list with maximum and minimum length. 
# 	Original list:
# 	[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 	List with maximum length of lists:
# 	(3, [13, 15, 17])
# 	List with minimum length of lists:
# 	(1, [0])
# 	Original list:
# 	[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists:
# 	(3, [3, 5, 7])
# 	List with minimum length of lists:
# 	(1, [0])
# 	Original list:
# 	[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists:
# 	(4, [1, 34, 5, 7])
# 	List with minimum length of lists:
# 	(1, [12])

l1 = [[0],[1, 3], [5, 7], [9, 11], [3, 5, 7]]
m = 0
min = len(l1[0])
tup1=None
tup2=(len(l1[0]),l1[0])
for i in l1:
    if len(i)>m:
        m = len(i)
        tup1 = (len(i),i)
    elif len(i)<min:
        min = len(i)
        tup2 = (len(i),i)
print("List with maximum length of lists:",tup1)
print("List with minimum length of lists:",tup2)

# 92. Write a Python program to check if a nested list is a subset of another nested list. 
# 		Original list:
# 		[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 		[[1, 3], [13, 15, 17]]
# 		If the one of the said list is a subset of another.:
# 		True
# 		Original list:
# 		[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# 		[[[3, 4], [5, 6]]]
# 		If the one of the said list is a subset of another.:
# 		True
# 		Original list:
# 		[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# 		[[[3, 4], [5, 6]]]
# 		If the one of the said list is a subset of another.:
# 		False

# 93. Write a Python program to count the number of sublists contain a particular element. 
# 		Original list:
# 		[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# 		Count 1 in the said list:
# 		3
# 		Count 7 in the said list:
# 		2
# 		Original list:
# 		[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# 		Count 'A' in the said list:
# 		3
# 		Count 'E' in the said list:
# 		1
l1 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
l2 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
c = 0
for i in l2:
    c += i.count(7)
print("Count in the list is : ",c)

# 94. Write a Python program to count number of unique sublists within a given list. 
# 	Original list:
# 	[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# 	Number of unique lists of the said list:
# 	{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
# 	Original list:
# 	[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# 	Number of unique lists of the said list:
# 	{('green', 'orange'): 2, ('black',): 1, ('white',): 1}
l1 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
l1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
dict1 = {}
for i in l1:
    c = 0
    for j in l1:
        if i==j:
            c+=1
    dict1[tuple(i)]=c
print(dict1)

# 95. Write a Python program to sort each sublist of strings in a given list of lists. 
# 	Original list:
# 	[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# 	Sort the list of lists by length and value:
# 	[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

l1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
l1.sort()
for i in range(len(l1)):
    for j in range(len(l1)-1):
        if len(l1[j])>len(l1[j+1]):
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)