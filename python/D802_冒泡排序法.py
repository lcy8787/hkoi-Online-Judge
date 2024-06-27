run = 0
a, b = map(int, input().split())
array = list(map(int, input().split()))

if a > 1:
    if b == 0:
        for i in range(0, a-1):
            for j in range(0, a-1-i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    run += 1
    elif b == 1:
        for i in range(0, a-1):
            for j in range(0, a-1-i):
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    run += 1

print(run)
print(" ".join(map(str, array)))

         