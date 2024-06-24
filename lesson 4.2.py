#value_list = [0, 1, 7, 2, 4, 8]
#first_list = value_list[::2]
#sum = sum(first_list)
#mult = sum * value_list[-1]
#print(mult)







value_list = [0, 1, 7, 2, 4, 8]
result = 0

for i in range(0, len(value_list), 2):
    result += value_list[i]

if value_list != []:
    result = result * value_list[-1]

print(result)







value_list = [0, 1, 7, 2, 4, 8]
result = 0

if value_list:
    result = sum(value_list[::2]) * value_list[-1]
print(result)

