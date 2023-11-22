def solve(n):
    l = []
    for i in range(1, n+1):
        result = (((10**i)-1)//9)**2
        l.append(result)
    return l