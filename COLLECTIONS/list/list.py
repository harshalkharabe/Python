"""List data type
Lists are mutable sequences, typically used to store collections of
homogeneous items or heterogeneous items.
How to create list?
list can be represented in different ways
1. Using empty square brackets to denote the empty list []
2. Within square brackets more than one item is defined by separating
with ,
[item,item,item,item], [item]
3. Using list comprehension
4. Using list function (type conversion)
a. list()
b. list(iterable)

Note: all collection types are called iterables, which can be iterated"""

l1 = []
print(l1,type(l1))
l2 = [12,34,23,14]
l3 = [1.23,3.44,23.12,11.4]
l4 = [12,"python",False,14.90]
print(l2,l3,l4,sep='\n')

"""list() function
This function is used to convert other iterables into list
Syntax-1: list() empty list
Syntax-2: list(iterable)  the construct list using existing iterable(OR)
convert other iterables into list type"""

l1 = list()
print(l1,type(l1))
l2 = list([12,9,34,66])
# l3 = list(10)
l4 = list("PYTHON")
l5 = list(range(10,101,10))
l6 = list(l2)

print(l2,l4,l5,l6,sep='\n')

"""How to read data or content from list or sequences?
1. Using index
2. Using slicing
3. Using for loop
4. Using iterator
5. Using enumerate"""

l1 = [10,20,30,40,50]

print("Forward indexing")
for i in range(0,5):
    print(l1[i],end=' ')

print()

print("Backward indexing")
for i in range(-5,0,1):
    print(l1[i],end=' ')

print()

print("Sum : ",sum(x:=list(range(10,101,10))),"list : ",x)

# Write a program to add or print sum,min,max & average of elements or items to find avg of list
l1 = list([12,45,3,67,89])
sum,min,max = 0,l1[0],0
for i in range(len(l1)):
    if max<l1[i]:
        max = l1[i]
    if min>l1[i]:
        min=l1[i]
    sum = sum + l1[i]
print(f"Sum of all items in list {l1} is {sum}")
print(f"Average of list {l1} is {sum/len(l1)}")
print(f"Maximun in list : {max}")
print(f"Minimum in list : {min}")


#WAP to find median of l1
l1 = [12,45,3,41,67,34,89]
length = len(l1)
if length%2==0:
    i = length//2
    median = (l1[i]+l1[i-1])/2
else:
    i = length//2
    median = l1[i]
print(f"Median : {median}")

list1 = list(range(1,51,1))
l1 = []
l2 = []
count = 0
for i in list1:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
    count += 1
    print(f"Numbers of elements in list : {count}")
print(f"Even numbers list : {l1}")
print(f"Odd numbers list : {l2}")

list1 = [12,34,10,2,34]
mean = 0
for i in list1:
    mean += i
print(f"Mean : {mean/len(list1)}")


import statistics
print(statistics.median([10,17,27,89]))
print(statistics.mode([122,17,27,89]))
print(statistics.mean([10,17,27,89]))

list1 = [23,45,12,32,9,2]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)


