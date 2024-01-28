'''
You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.
'''

from collections import Counter

n = int(input())

words = [input() for _ in range(n)]
output = Counter(words)
print(len(output))

for _ in output.values():
    print(_, end=' ')