s = input("Enter a String:")
s_o = dict()
for i in s:
    count = s.count(i)
    print(count)
    s_o[i] = count

print('Result:', s_o)
       