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


#my_list = [9, 0, 7, 31, 0, 45, 0, 0, 96, 0]
#second_list = []
#
#zero = my_list.count(0)
#
#for index in range(len(my_list)):                  too compicated
  #  if my_list[index] != 0:
 #       second_list.append(my_list[index])
#
#second_list.extend([0] * zero)
#
#print(second_list)

#my_list = [9, 0, 7, 31, 0, 45, 0, 0, 96, 0]

#for index in range(len(my_list)):
   # if my_list[index] == 0:
  #      my_list.remove(0)
 #       my_list.append(0)
#
#print(my_list)


#my_list = [9, 0, 7, 31, 0, 45, 0, 0, 96, 0]

#my_list.sort(reverse=True, key=bool)

#print(my_list)





