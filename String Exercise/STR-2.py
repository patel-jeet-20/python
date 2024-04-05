# Create a string made of the middle three characters
s = input("Enter a String:")
l = len(s) // 2
res = s[l - 1] + s[l] + s[l + 1]
print(res)
