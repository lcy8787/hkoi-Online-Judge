array = []
run = int(input())
def push(num):
    array.append(num)
def top():
    if len(array) != 0:
        return array[len(array)-1]
    else:
        return "Empty"
        
def pop():
    if len(array) != 0:
        array.pop(len(array)-1)
    else:
        print("Cannot pop")
def size():
    print(len(array))

for i in range(0,run):
    do = input().split()
    if do[0] == "PUSH":
        push(do[1])
    elif do[0] == "TOP":
        print(top())
    elif do[0] == "POP":
        pop()
    elif do[0] == "SIZE":
        size()