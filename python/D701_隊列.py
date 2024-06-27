array = []
run = int(input())
def push(num):
    array.append(num)
def front():
    if len(array) != 0:
        return array[0]
    else:
        return "Empty"
        
def pop():
    if len(array) != 0:
        array.pop(0)
    else:
        print("Cannot pop")
def size():
    return len(array)
for i in range(0,run):
    do = input().split()
    if do[0] == "PUSH":
        push(do[1])
    elif do[0] == "FRONT":
        print(front())
    elif do[0] == "POP":
        pop()
    elif do[0] == "SIZE":
        print(size())

    