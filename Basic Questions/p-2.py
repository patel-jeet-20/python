def addition(a):
    p = 0
    for i in range(0, a):
        r = p + i
        print(f"Current number is {i} and the previous number is {p} sum:", r)
        p = i


n = int(input("Enter an integer:"))
addition(n)