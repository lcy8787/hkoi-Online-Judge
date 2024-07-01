S = list(input().strip())
N = int(input().strip())

for _ in range(N):
    check = list(input().strip())
    temp_S = S.copy()
    can_form = True
    
    for char in check:
        if char in temp_S:
            temp_S.remove(char)  
        else:
            can_form = False
            break
    
    if can_form:
        print("Yes")
    else:
        print("No")