sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
r_list = list()

for u in sample_list:
    if u not in r_list:
        r_list.append(u)
print(r_list)
r_tuple = tuple(r_list)
print(r_tuple)
print(min(r_tuple))
print(max(r_tuple))
