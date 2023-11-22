def solve(str1):
    l = []
    f = []
    for i in str1:
        if i not in l:
            l.append(i)
            f.append(1)
        else:
            index = l.index(i)
            f[index] += 1
    return f