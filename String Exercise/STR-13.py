S_l = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
r_l = []
for i in S_l:
    if i:
        r_l.append(i)

print(r_l)

n_s_l = list(filter(None, S_l))
print(n_s_l)