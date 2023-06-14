#a = input()
n, m = map(int, input().split(' '))
for i in range(n // 2):
    pattern = '.|.' * (2 * i + 1)
    print(pattern.center(m, '-'))
message = 'WELCOME'
print(message.center(m, '-'))
for i in range(n // 2 - 1, -1, -1):
    pattern = '.|.' * (2 * i + 1)
    print(pattern.center(m, '-'))
