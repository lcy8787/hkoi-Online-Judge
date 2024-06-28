a = int(input())
array = list(map(int, input().split()))
print(array[0])

for i in range(1, a):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
    print(" ".join(map(str, array[:i+1])))

