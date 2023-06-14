if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        t = list(map(str, input().split(" ", -1)))
        if (t[0] == 'insert'):
            a.insert(int(t[1]), int(t[2]))
        elif (t[0] == 'print'):
            print(a)
        elif (t[0] == 'remove'):
            a.remove(int(t[1]))
        elif (t[0] == 'append'):
            a.append(int(t[1]))
        elif (t[0] == 'sort'):
            a.sort()
        elif (t[0] == 'pop'):
            a.pop()
        elif (t[0] == 'reverse'):
            a.reverse()
