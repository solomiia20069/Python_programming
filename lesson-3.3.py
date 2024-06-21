#my_list = [1, 2, 3, 4, 5, 6]
#print(my_list[0:3], my_list[3:6])

#value_list = [1, 2, 3]
#print(value_list[0:2], value_list[2:])

#list_1 = [1, 2, 3, 4, 5]
#print(list_1[0:3], list_1[3:5])

#list_2 = [1]
#print(list_2[:], list_2[:0])

#list_3 = []
#print(list_3[:], list_3[:])


#list3 : str[input("enter list:")] ??? пробувала експерементувати з інпутами і сплітом в лістах
#print(list3.split("")) ???

my_list = [1, 2, 3, 4, 5, 6]

separator = len(my_list) - len(my_list) // 2
new_list = [my_list[:separator], my_list[separator:]]

print(new_list)