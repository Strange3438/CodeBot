from collections import Counter
a = list()
n = int(input())
count = 0
for i in range(n):
    a.append(input())
b = Counter(a)
print(len(b))
for i in b.values():
    print(i, end = " ")
