my_list = [9, 0, 7, 31, 0, 45, 0, 0, 96, 0]
result = []
count = 0
for i in my_list:
    if i == 0:
        count += 1
    else:
        result.append(i)
result += [0] * count

print(result)