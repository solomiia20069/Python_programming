def add_one(some_list):

    string_list = [str(i) for i in some_list]
    digit = int("".join(string_list))
    add_digit = digit + 1
    new_list = list(map(int, str(add_digit)))

    return new_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
