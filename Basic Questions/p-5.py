# checking if first element in one list and last element in second list are same or not
def check():
    a = []
    b = []
    n = int(input("Enter the total number of elements to be append in a list:"))
    print("List a:")
    for i in range(1, n+1):
        i = int(input())
        a.append(i)
    print("List b:")
    for i in range(1, n+1):
        i = int(input())
        b.append(i)

    print(f"First list = {a}")
    print(f"Second list = {b}")

    if a[0] == b[-1]:
        return True
    else:
        return False


print(check())
