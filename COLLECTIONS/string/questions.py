#Remove duplicates in string
# s1 = input("Enter string : ")
# s2 = ''

# for i in s1:
#     if i not in s2:
#         s2 += i
# print(f"After Removing Duplicates : {s2}")

# #PYTHON PROGRAM TO GIVE LEAST FREQUENCY (COUNT) OF CHARACTER
# s1 = "python programming"
# s2 = ''
# for i in s1:
#     if i not in s2:
#         s2 += i
# mcount = s1.count(s1[0])
# print(s2)
# ch = s1[0]
# for i in s2:
#     c = s1.count(i)
#     if mcount>c:
#         mcount=c
#         ch = i
#         print(True)
# print(ch,"-->",mcount)


# #ALL FREQUENCY OF CHARACTERS IN STRING
# s1 = input("Enter a string : ")
# S2 = ''
# for ch in s1:
#     if ch not in S2:
#         S2 += ch
# print(S2)
# s3 = ''
# for i in S2:
#     s3 = s3+str(s1.count(i))+i
# print(s3)

## Python program to check whether the string is
# Symmetrical or Palindrome

# s1 = input("Enter a string : ")
# s2 = ''
# s2 = s1[::-1]
# if s1==s2:
#     print(f"{s1} is palindrome string")
# else:
#     print(f"{s1} is not palindrome string")

# if len(s1)%2==0:
#     l = len(s1)//2
#     s3=s1[:l]
#     s4=s1[l:]
#     if s3 == s4:
#         print(f"{s1} is symmetrical string")
#     else:
#         print(f"{s1} is not symmetrical string")
# else:
#     print(f"{s1} is not symmetrical string")

#input : 1b3c4d
#output : bcccdddd

s1 = input("Enter input : ")
s2 = ''
i=0
while i<len(s1)-1:
    digit = s1[i]
    i+=1
    ch = s1[i]
    s2=s2+(ch*int(digit))
    # for i in range(int(digit)):
    #     s2 = s2+ch
    i+=1
print(s1,s2)