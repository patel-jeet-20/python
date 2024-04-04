# Create a function with variable length of arguments
def add(*addition):
    c = 0
    for i in addition:
        c += i
    print(c)


add(10, 20, 30)
