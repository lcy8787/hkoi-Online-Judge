N, H = map(int, input().split())
array = list(map(int, input().split()))
target = list(map(int, input().split()))

for i in range(0,N+1):
    if H == 0:
        print("End")
        break
    else:
        print(array[H-1])
        H = target[H-1]
        
         