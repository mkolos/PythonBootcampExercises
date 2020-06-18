def gencubes(n):
    for num in range(n):
        yield num ** 3


for x in gencubes(10):
    print(x)


# 0
# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729

def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for num in genfibon(10):
    print(num)


#
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55


def simple_gen():
    for x in range(3):
        yield x


g = simple_gen()
print(next(g))
# 0
print(next(g))
# 1
