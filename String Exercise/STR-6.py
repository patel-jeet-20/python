s1 = input("Enter a string:")
s2 = input("Enter a string:")

l_s1 = len(s1)
l_s2 = len(s2)

l = l_s1 if l_s1 > l_s2 else l_s2
res = ''
s2 = s2[::-1]
for i in range(l):
    if i < l_s1:
        res += s1[i]
    if i < l_s2:
        res += s2[i]

print(res)
