def mul_and_sum(a, b):
    c = a*b
    d = a+b
    if c <= 1000:
        return c
    else:
        return d


print(mul_and_sum(5, 1000))