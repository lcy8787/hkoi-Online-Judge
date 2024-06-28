alen, blen = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
array = [0] * (alen + blen)  

i = 0
j = 0
for k in range(alen + blen):
    if i < alen and (j == blen or a[i] < b[j]):
        array[k] = a[i]
        i += 1
    else:
        array[k] = b[j]
        j += 1

print(" ".join(map(str, array[:i+1])))