from itertools import product
a = list(map(int, input().split(" ", -1)))
b = list(map(int, input().split(" ", -1)))
d = list(product(a, b))
for i in d:
    print(i, end = " ")
