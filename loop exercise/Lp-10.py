n = int(input("Enter an integer:"))
l = []
for i in range(1, n + 1, 1):
    l.append(i)
    res = list(map(lambda x: x ** 3, l))
print(res)
