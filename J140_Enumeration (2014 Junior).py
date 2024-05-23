N = int(input())
for i in range(1, N+1):
    line = [i**2 + j*i for j in range(N)]
    print(' '.join(map(str, line)))
