N = int(input())
numbers = list(map(int, input().split()))

max_num = float('-inf')
second_max_num = float('-inf')

for num in numbers:
    if num >= max_num:
        second_max_num = max_num
        max_num = num
    elif num >= second_max_num and num != max_num:
        second_max_num = num

print(max_num)
print(second_max_num)