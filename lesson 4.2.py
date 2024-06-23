value_list = [0, 1, 7, 2, 4, 8]
first_list = value_list[::2]
sum = sum(first_list)
mult = sum * value_list[-1]
print(mult)