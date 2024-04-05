s = input("Enter a String:")
num = 0
d_c = 0
for i in s:
    if i.isdigit():
        num += int(i)
        d_c += 1

result = num / d_c
print(result)
