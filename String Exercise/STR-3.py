#  Append new string in the middle of a given string
s = input("Enter a string:")
t = input("Enter extended string:")
l = len(s) // 2
res = s[:l] + t + s[l:]
print(res)