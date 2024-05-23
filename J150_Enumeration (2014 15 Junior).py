def print_pattern(N):
    num = 1
    for i in range(N):
        line = [str(num + j*4) for j in range(N)]
        print(' '.join(line))
        if i != N-1:
            num = num + 4*(N-1)

N = int(input())
print_pattern(N)
