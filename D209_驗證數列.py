N = int(input())
numbers = list(map(int, input().split()))
ans = "Valid"
for i in range(N):
    if numbers[i] <= 100 or numbers[i] >= 50000:
        ans = "Invalid"

if len(set(numbers)) != N:
    ans = "Invalid"

for i in range(N - 1):
    if numbers[i] > numbers[i + 1]:
        ans = "Invalid" 

print(ans)