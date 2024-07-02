main = input()
second = input()

total_count = 0
for i in range(len(main) - len(second) + 1):
    if main[i:i+len(second)] == second:
        total_count += 1


non_over_count = 0
i = 0
while i <= len(main) - len(second):
    if main[i:i+len(second)] == second:
        non_over_count += 1
        i += len(second)  
    else:
        i += 1

print(total_count)
print(non_over_count)
    

