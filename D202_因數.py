def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    
    factors.sort()
    return factors

N = int(input())

factors = find_factors(N)

for factor in factors:
    print(factor)