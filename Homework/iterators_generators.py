import random


def gensquares(N):
    for x in range(N):
        yield x ** 2


for x in gensquares(10):
    print(x)


def rand_num(low, high, n):
    sum = 0
    while sum < n:
        yield random.randint(low, high)
        sum += 1


for num in rand_num(1, 10, 12):
    print(num)


def make_string_iterable(s):
    for letter in s:
        yield letter


iterable_string = make_string_iterable('hello')
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
