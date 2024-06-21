value_list = [1, 2, 4, 6]
first_element = value_list.pop(0)
last_element = value_list.pop(-1)
value_list.insert(0, last_element)
value_list.append(first_element)

print(value_list)

original_list = [12, 5, 6, 7, 8]

if len(original_list) > 1:
    last_element = original_list.pop()
    original_list.insert(0,last_element)

print(original_list)