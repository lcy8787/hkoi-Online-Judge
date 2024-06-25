check_len ,find_len = map(int, input().split())
check_array = list(map(int, input().split()))
target = list(map(int, input().split())) 

for i in range(0,find_len):
  start = 0 
  end = check_len - 1
  found = False
  while start <= end:
    mid = (start + end) // 2
    if check_array[mid] == target[i]:
      found = True
      break
    elif check_array[mid] > target[i]:
      end = mid - 1
    else:
      start = mid + 1
  if found:
    print("Yes")
  else:
    print("No")