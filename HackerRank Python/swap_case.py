def swap_case(s):
    a = ""
    for i in s:
        if i.isupper():
            a += i.lower()
        elif i.islower():
            a += i.upper()
        else:
            a += i
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
