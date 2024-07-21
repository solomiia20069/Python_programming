def prime_generator(num):
    if num < 2:
        return
    yield 2

    filter = [True] * (num + 1)
    for i in range(3, num +1, 2):
        if filter[i]:
            yield i
            for multiple in range(i * i, num + 1, i):
                filter[multiple] = False


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
