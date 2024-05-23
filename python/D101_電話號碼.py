# 讀取輸入的電話號碼
phone_number = input()

# 檢查電話號碼長度是否為八位數字
if len(phone_number) == 8:
    # 提取首位數字
    first_digit = int(phone_number[0])

    # 判斷電話號碼類型並輸出結果
    if first_digit == 2 or first_digit == 3:
        print("Fixed")
    elif first_digit == 5 or first_digit == 6 or first_digit == 9:
        print("Mobile")