list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# -> Using List Comprehension
list3 = [a + d for a in list1 for d in list2]
print(list3)

# ->Without Using list comprehension
list4 = []
for i in list1:
    for n in list2:
        res = i + n
        list4.append(res)

print(list4)
