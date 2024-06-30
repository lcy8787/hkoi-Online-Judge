array = []
price = [0, 0]

N = int(input())
for i in range(N):
    temp = list(map(float, input().split()))
    array.append(temp)
    
M = int(input())
for j in range(M):
    check = input().split()
    start = int(check[0]) - 1
    end = int(check[1]) - 1
    ticket_type = check[2]
    
    if ticket_type == "A":
        if start < end:
            price[0] = array[start][end]
        else:
            price[0] = array[end][start]
    else:  # ticket_type == "C"
        if start < end:
            price[0] = array[end][start]
        else:
            price[0] = array[start][end]
    
    print(f"{price[0]:.1f}")