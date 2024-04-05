# create a string made of first, last and middle character
s = input("Enter a String:")
res = ' '
a = s[0]
res += a
b = len(s)//2
res += s[b] + s[-1]
print(res)
