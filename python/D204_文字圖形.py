N = int(input())

if N % 2 == 0:
    N += 1  


if N != 1:
    for i in range(N//2):
        spaces_before = " " * (N//2 - i)
        if i == 0:
            print(spaces_before + "#")
        else:
            spaces_between = " " * (2 * i - 1)
            print(spaces_before + "#" + spaces_between + "#")
            
    if N != 1:
        spacem = " " * (N - 2)
        print("#" + spacem + "#")
        
    for i in range(N//2, 0, -1):
        spaces_before = " " * (N//2 - i + 1)
        if i == 1:
            print(spaces_before + "#")
        else:
            spaces_between = " " * (2 * (i - 1) - 1)
            print(spaces_before + "#" + spaces_between + "#")
            
else:
    print("#")