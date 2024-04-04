n = int(input("Enter an integer:"))
result = 0
while n > 0:
    rem = n % 10
    result = (result * 10) + rem
    n //= 10
print(result)