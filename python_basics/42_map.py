def add(x):
    return x+2

newlist = [10, 20, 30, 40 ,50]

result = list(map(add, newlist))

lambdas = list(map(lambda x: x*2, newlist))

print(result)