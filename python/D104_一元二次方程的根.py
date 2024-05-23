import math

# 讀取輸入的係數 a、b 和 c
a, b, c = map(float, input().split())

# 判斷 a 是否為 0，或者 a、b、c 是否超出範圍，如果是則不輸出結果
if a == 0 or abs(a) > 100 or abs(b) > 100 or abs(c) > 100:
    pass
else:
    # 計算判別式
    discriminant = b**2 - 4*a*c

    # 判斷根的情況並輸出結果
    if discriminant < 0:
        # 沒有實根
        print("None")
    elif discriminant == 0:
        # 只有一個實根
        root = -b / (2*a)
        formatted_root = "{:.3f}".format(root)
        print(formatted_root)
    elif discriminant > 0:
        # 有兩個實根
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        # 確保 root1 是數值較小的根
        if root1 > root2:
            root1, root2 = root2, root1
        
        formatted_root1 = round(root1,3)
        formatted_root2 = round(root2,3)
        print("{:.3f}".format(formatted_root1), "{:.3f}".format(formatted_root2))