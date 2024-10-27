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
