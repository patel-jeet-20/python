def new_list():
    a = []
    b = []
    n = int(input("Enter the total number of elements to be append in a list:"))
    print("List a:")
    for i in range(1, n + 1):
        i = int(input())
        a.append(i)
    print("List b:")
    for i in range(1, n + 1):
        i = int(input())
        b.append(i)

    print(f"First list = {a}")
    print(f"Second list = {b}")
    a.extend(b)
    print(f"New List = {a}")


new_list()