n = int(input("Enter the range of list:"))
l = []
for i in range(n):
    m = int(input(f"Enter {i+1} Element in a list:"))
    l.append(m)
print(l)

for i in l:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
    else:
        pass

