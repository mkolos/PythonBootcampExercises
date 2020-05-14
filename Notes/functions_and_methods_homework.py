import string


def vol(rad):
    return (rad ** 3) * 3.14 * (4 / 3)


print(vol(2))


def ran_check(num, low, high):
    return num in range(low, high)


print(ran_check(3, 1, 10))


def up_low(s):
    letters = {'upper': 0, 'lower': 0}
    for letter in s:
        if letter.isupper():
            letters['upper'] += 1
        elif letter.islower():
            letters['lower'] += 1

    return 'No. of Upper case characters : {} \nNo. of Lower case Characters : {}'.format(letters['upper'],
                                                                                          letters['lower'])


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))


def unique_list(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


def multiply(numbers):
    sum = 1
    for item in numbers:
        sum *= item

    return sum


print(multiply([1, 2, 3, -4]))


def palindrome(s):
    return s == s[::-1]


print(palindrome('helleh'))


def ispangram(str1, alphabet=string.ascii_lowercase):
    for letter in alphabet:
        if letter not in str1.lower():
            return False

    return True


print(ispangram("The quick brown fox jumps over the lazy dog"))