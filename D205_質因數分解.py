def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# 讀取輸入
n = int(input())

# 因式分解為質數的積
factors = prime_factorization(n)

# 輸出結果
result = str(n) + "=" + "*".join(map(str, factors))
print(result)
