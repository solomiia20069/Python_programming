value_list = [12, 3, 4, 10]
first_element = value_list.pop(0)
last_element = value_list.pop(-1)
value_list.insert(0, last_element)
value_list.append(first_element)

print(value_list)
