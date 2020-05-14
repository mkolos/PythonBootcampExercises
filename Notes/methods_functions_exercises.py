def lesser_of_two_evens(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return min(x, y)
    return max(x, y)


def animal_crackers(string):
    words = string.split()
    if words[0][0] == words[1][0]:
        return True

    return False


def makes_twenty(x, y):
    if x == 20 or y == 20 or sum((x, y)) == 20:
        return True

    return False


def old_macdonald(name):
    if len(name) > 3:
        return name[0:3].capitalize() + name[3:].capitalize()

    return 'Name is too short'


def master_yoda(sentence):
    words = sentence.split()
    words.reverse()

    return ' '.join(words)


def almost_there(number):
    if abs(number - 100) > 10 and abs(number - 200) > 10:
        return False

    return True


def has_33(list_of_ints):
    for i in range(0, len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True

    return False


def paper_doll(text):
    new_string = ''
    for letter in text:
        new_string += letter * 3

    return new_string


def blackjack(a,b,c):
    sum_of_numbers = sum((a, b, c))
    if sum_of_numbers <= 21:
        return sum_of_numbers
    elif a == 11 or b == 11 or c == 11:
        return sum_of_numbers - 10

    return 'BUST'


def summer_69(array):
    i = 0
    blocked_numbers = [6, 7, 8, 9]
    reduced_array = []
    for number in array:
        if number in blocked_numbers:
            continue
        reduced_array.append(number)

    return sum(reduced_array)


def spy_game(nums):
    spy = []
    for num in nums:
        if num == 7 or num == 0:
            spy.append(num)

    return spy == [0, 0, 7]


def count_primes(num):
    quantity_of_primes = 0
    for item in range(2, num):
        is_prime = True
        for i in range(2, item):
            if item % i == 0:
                is_prime = False
                break
        if is_prime:
            quantity_of_primes += 1

    return quantity_of_primes


print(count_primes(100))