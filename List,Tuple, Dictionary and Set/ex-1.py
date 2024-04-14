l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []
l4 = []

for i in l1[1::2]:
    l3.append(i)

for j in l2[::2]:
    l4.append(j)

print(f"Element at odd-index positions from list one:\n{l3}")
print(f'Element at even-index positions from list two:\n{l4}')

l3.extend(l4)
print(f'New list combining l3 and l4 is:\n{l3}')
