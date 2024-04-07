list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# -> using list comprehension
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)

# without using list comprehension
list3 = []
for i, j in zip(list1, list2):
    res = i + j
    list3.append(res)
print(list3)
