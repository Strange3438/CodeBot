if __name__ == '__main__':
    b = list()
    for _ in range(int(input())):
        a = list()
        name = input()
        score = float(input())
        a.append(name)
        a.append(score)
        b.append(list(a))
        
    grades = list()
    for i in b:
        grades.append(i[1])
    value = min(grades)
    while value in grades:
        grades.remove(value)
    minGrade = min(grades)
    names = []
    for i in b:
        if (i[1] == minGrade):
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)
