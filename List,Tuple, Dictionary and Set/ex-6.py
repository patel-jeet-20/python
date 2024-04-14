first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
res = first_set.intersection(second_set)
print(res)
for i in res:
    first_set.remove(i)

print(first_set)