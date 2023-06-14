from collections import Counter
x = int(input())
sizes = list(map(int, input().split(' ')))
n = int(input())
amount = 0
a = Counter(sizes)
#print(Counter(sizes).items())
for i in range(n):
    s, x = map(int, input().split(' '))
    for i in a.keys():
        if s == i and a[i] > 0:
            amount += x
            a[i] -= 1
print(amount)
