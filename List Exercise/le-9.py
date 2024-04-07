list1 = [5, 20, 15, 20, 25, 50, 20]
val = int(input("Enter the value to be removed:"))
res = [i for i in list1 if i != val]
print(res)