def revere_no(n):
    res = 0
    while n > 0:
        rem = n % 10
        res = (res*10) + rem
        n //= 10
    print(res)


n = int(input("Enter an integer:"))
revere_no(n)
