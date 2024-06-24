import random

count = random.randint(2, 10)
my_list = [random.randint(1, 100) for i in range(count)]

print(my_list)


############## all other possible solutions ###############

#import random

#count = random.randint(2, 10)
#my_list = [random.randint(1, 100)** 2 for i in range(count)if i % 2]

#print(my_list)






#import random

#count = random.randint(3,10)

#value_list = []
#for i in range(count):
 #   value_list.append(random.randint(1, 100))


#print(value_list)

#if len(value_list) >= 3:

  #  new_list = [value_list[0], value_list[2], value_list[-2]]
 #   print(new_list)
#else:
  #  print('not enough elements in list')



