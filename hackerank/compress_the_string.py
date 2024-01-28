'''
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function

A single line of output consisting of the modified string.
'''

from itertools import groupby

if __name__ == '__main__':
    numbers = input()

    output = ""

    for i, g in groupby(numbers):
        times = len([j for j in g])
        output += f"({times}, {i})"

    print(output)