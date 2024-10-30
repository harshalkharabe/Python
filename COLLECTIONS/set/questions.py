s1 = {1,11,2,2,1}
print(len(s1))
s2 = set()
print(s2)
l1 = list()
print(l1)
s3 = {(1,2,3)}
print(s3)

#hash value always integer

n = 12
print(hash(n))

n1 = 1245
print(hash(n1))

n2 = 1245.23
print(hash(n2))

n5 = (1,2,3)
print(hash(n5))

n3 = [1,23,4] # list is not hashable
# n6 = {[12,2],[3,4]} # Not Allowed
# print(hash(n3))
#mutable objects are not hashable
n4 = {1,2,3} # set is also not hashable 
# print(hash(n4))

r = {10,10,20,30,40,50}
print(r)

s1 = {10,20,30,40,50}
print(s1)

s3 = {(1,2,3),(4,5,6),(7,8,9)}
print(s3)

s5 = {10,30,20,40,50}
print("Using For loop")
# Using For Loop
for i in s5:
    print(i)

#Using iterator()
print("Using Iterator Object")
a = iter(s5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

#Using enumerate
print("Using Enumerate Object")
b = enumerate(s5)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

f = 12.45454
print(round(f,2))

s1 = {10,20,30,40,50}
print(s1)
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())

s1={1,2,3}
s2={4,5,6}
print(s1.union(s2))

s1={1,2,3,4}
s2={1,2,3,4,5}
s3={1,2,4,5,6,7,8}
s4 = s1&s2-s3
print(s4)

s2 = set({'a':1,'b':3})
print(s2)

# s1 = {val for i in range(1,11) if (val:=int(input()))%2==0}
# print(s1)

#UNION
s1 = {1,2,4}
s2 = {3,5,6}
print(s1.union(s2))
#UPDATE
s1 = {1,2,4}
s2 = {3,5,6}
s1.update(s2)
print(s1)
#INTERSECTION
s1 = {1,2,4}
s2 = {3,5,6}
print(s1.intersection(s2))
#INTERSECTION_UPDATE
s1 = {1,2,4}
s2 = {3,5,6}
s1.intersection_update(s2)
print(s1)