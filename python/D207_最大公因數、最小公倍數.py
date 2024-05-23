def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm
n, m = map(int, input().split())
gcd = find_gcd(n, m)
lcm = find_lcm(n, m)
print(gcd)
print(lcm)