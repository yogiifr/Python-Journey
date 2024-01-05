from itertools import count, accumulate, takewhile

for i in count():
    print(i)

    if i >= 20:
        break

numbers = list(accumulate(range(8)))
print(numbers)

whilestate = list(takewhile(lambda x: x <= 10, numbers))
print(whilestate)