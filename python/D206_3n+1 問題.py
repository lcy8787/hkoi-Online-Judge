def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# 讀取輸入的整數 N
N = int(input())

# 生成序列
sequence = collatz_sequence(N)

# 輸出序列中的數字
for num in sequence:
    print(num)