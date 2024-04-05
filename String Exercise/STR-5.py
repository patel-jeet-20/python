s = input("Enter a string:")
upper = []
lower = []
for i in s:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)

res = ''.join(lower + upper)
print(res)
