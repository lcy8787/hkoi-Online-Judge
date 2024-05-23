def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        fib_list = [0, 1]
        for i in range(2, x + 1):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list[x]


x = int(input())
fib_x = f(x)
print(fib_x)