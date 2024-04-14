sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
l = len(sample_list)//3
print(l)
c1 = sample_list[:3]
c1.reverse()
c2 = sample_list[3:l+3]
c2.reverse()
c3 = sample_list[l+3:]
c3.reverse()
print(f'chunk 1 {sample_list[:3]} After reversing it {c1}')
print(f'chunk 1 {sample_list[3:l+3]} After reversing it {c2}')
print(f'chunk 1 {sample_list[l+3:]} After reversing it {c3}')
