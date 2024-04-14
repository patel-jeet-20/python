sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_digit = dict()
for i in sample_list:
    if i in count_digit:
        count_digit[i] += 1
    else:
        count_digit[i] = 1

print(count_digit)
