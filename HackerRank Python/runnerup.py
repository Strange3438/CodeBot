if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxElement = max(arr)
    b = list()
    for i in arr:
        if (i != maxElement):
            b.append(i)
    print(max(b))
