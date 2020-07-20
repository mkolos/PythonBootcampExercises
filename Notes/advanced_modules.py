from collections import Counter

# Collections
lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
Counter(lst)
# Counter({1: 6, 2: 6, 3: 4, 12: 1, 21: 1, 32: 1, 223: 1})

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

Counter(words)
#Counter({'How': 1,
         # 'does': 1,
         # 'each': 3,
         # 'in': 1,
         # 'many': 1,
         # 'sentence': 1,
         # 'show': 1,
         # 'this': 1,
         # 'times': 2,
         # 'up': 1,
         # 'word': 3})

# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts

