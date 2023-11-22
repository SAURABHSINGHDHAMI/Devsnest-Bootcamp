def solve(n, arr, x, y):
    s = sum(arr[x:y+1])
    l = len(arr[x:y+1])
    avg = s / l
    return avg