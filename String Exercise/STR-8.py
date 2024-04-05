s1 = input("Enter a string:")
s2 = input("Enter substring:")

res = s1.lower()
num = res.count(s2.lower())
print(num)