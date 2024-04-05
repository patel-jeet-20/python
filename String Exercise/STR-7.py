# String Character balance test
def balance(s1, s2):
    flag = True
    if s2 in s1:
        return flag
    else:
        flag = False
        return flag


s1 = input("Enter a string:")
s2 = input("Enter a substring:")
print(balance(s1, s2))
