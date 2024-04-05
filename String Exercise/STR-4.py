#  Append new string in the middle of a given string

s1 = input("Enter first String:")
s2 = input("Enter second string:")
res = ' '
res += s1[0] + s2[0]
l1 = len(s1)//2
l2 = len(s2)//2
res += s1[l1] + s2[l2] + s1[-1] + s2[-1]
print(res)
