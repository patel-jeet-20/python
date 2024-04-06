def primr(st, end):
    for i in range(st, end+1):
        if i > 1:
            for num in range(2, i):
                if i % num == 0:
                    break
            else:
                print(i)


n = int(input("Enter start Integer:"))
m = int(input("Enter ending Integer:"))
primr(n, m)
