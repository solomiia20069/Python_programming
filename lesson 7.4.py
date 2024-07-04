def common_elements():
    mult_3 = {num for num in range(100) if num % 3 == 0}

    mult_5 = {num for num in range(100) if num % 5 == 0}

    inter = mult_3.intersection(mult_5)

    return inter
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print(common_elements())