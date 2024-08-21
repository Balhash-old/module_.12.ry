numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prims = []
not_prims = []
for i in numbers:
    for j in range(2, i+1):
        if i % j == 0 and i != j:
            not_prims.append(i)
            break
        elif i == j:
            prims.append(i)
        else:
            continue
print('простые числа:', prims)
print('не простые числа:', not_prims)



