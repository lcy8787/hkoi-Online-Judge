# 讀取產品數量和建立產品資料庫
n = int(input())
products = {}
for _ in range(n):
    barcode, price = input().split()
    products[barcode] = float(price)

# 處理顧客購物車和計算總價
total_price = 0
m = int(input())
for _ in range(m):
    barcode = input()
    if barcode in products:
        total_price += products[barcode] 

# 輸出總價
print(f"{total_price:.1f}")