def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

map(square, my_nums)

for item in map(square, my_nums):
    print(item)


# [1, 4, 9, 16, 25]

def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]

my_list = list(filter(check_even, my_nums))
# [0, 2, 4, 6]

list(map(lambda num: num ** 2, my_nums))
# [1, 4, 9, 16, 25]

list(filter(lambda n: n % 2 == 0, nums))
# [0, 2, 4, 6, 8, 10]
