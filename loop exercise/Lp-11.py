def series(n, r):
    res = 0
    a = n
    for i in range(r):
        res += n
        n = (n*10)+a
    print(res)


n = int(input("Enter series integer:"))
r = int(input("Enter Range:"))
series(n, r)
