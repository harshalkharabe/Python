#FIND Nth MAXIMUM AND MINIMUM ELEMENT IN TUPLE

t1 = (3,77,7,7,1)
k=2
l1 = sorted(t1)
mi = l1[:k]
mx = l1[-k:]
t2 = tuple(mi+mx)
print(t2)

#python program to find cudes of given list values
#INPUT = [9,5,2,6,8]
#INPUT = [(9,729),(5,125),(2,8),(6,),(8,)]

l1 = [9,5,2,6,8]
l2 = [(num,num**3) for num in l1]
print(l2)

#ADDING TUPLE INTO LIST AND VISE VERSA

l1 = [12,34,56,32]
t1 = (2,4,5,3)
print(l1+list(t1))
print(t1+tuple(l1))

#Sum of tuple elements

T1 = (12,34,56,78,54)
s=0
for i in T1:
    s += i
print(f"Sum : {s}")

#Multiply Adjacent elements
t1 = (12,2,13,3,14,4,15,5)
l2 = []
for i in range(len(t1)-1):
    l2.append(t1[i]*t1[i+1])
print(f"Multiplying Adjucent Elements : {tuple(l2)}")

# Join Tuples if similar initial element
# Input : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)]

t1 = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
l1 = []
for i in t1:
    l = list(i)
    l1.append(l)
print(l1)


#FIBONACII SERIES

n1 = 0
n2 = 1
n3 = 0
print(f"Fibonacii Series : {n1},{n2}",end=' ')
while n3<55:
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3,end=' ')