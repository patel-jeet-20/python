n = int(input("Enter an integer:"))
count_num = 0
while n != 0:
    n //= 10
    count_num += 1
print(count_num)