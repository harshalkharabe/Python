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

