def find_unique_value(some_list):
    count_dict = {}

    for num in some_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count == 1:
            return num


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК")

#######################second possible version########################

#from collections import Counter
#
#def find_unique_value(some_list):
#    count_dict = Counter(some_list)
#
#    for num, count in count_dict.items():
#        if count == 1:
#            return num
#
#assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
#assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
#assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
#
#print("OK")