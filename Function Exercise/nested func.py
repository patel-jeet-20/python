def outer(x, y):

    def inner(a, b):
        anas = a + b
        return anas

    # ans = inner(x, y)
    # return ans
    return inner(x, y)


print(outer(5, 1))