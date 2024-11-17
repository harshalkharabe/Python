def ispal(s):
    return s==s[::-1]

def isprime(num):
    for i in range(2,num):
        if i%2==0:
            return False
    return True

def ispalnum(num):
    num1=num
    res = 0
    while num>0:
        d = num%10
        res = (res*10)+d
        num = num//10
    return res==num1