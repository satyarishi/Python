from collections import Counter


def word_count(filename):
    with open(filename) as f:
        return Counter(f.read().split())


counter = word_count('E:/python/explore.txt')
for i in counter:
    print(i, ':', counter[i])
