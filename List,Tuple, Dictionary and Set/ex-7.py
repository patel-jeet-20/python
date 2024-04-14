first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print(f'First set is a subset io Second Set:{first_set.issubset(second_set)}')
print(f'Second set is a subset of First Set:{second_set.issubset(first_set)}')
print('\n')
print(f'First set is a super set of Second set:{first_set.issuperset(second_set)}')
print(f'Second set is a super set of first set:{second_set.issuperset(first_set)}')

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()
print('\n')
print(f'First Set:\n{first_set}')
print(f'Second Set:\n{second_set}')
