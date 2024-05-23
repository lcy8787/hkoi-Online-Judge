def input_string():
    ans = input()
    return ans

def geez(ans):
    v = len(ans)
    k = ['_'] * v
    win = 0
    while win != 1:
        guess = input()
        for i in range(v):
            if guess == ans[i]:
                k[i] = ans[i]
        print(''.join(k))
        if ''.join(k) == ans:
            win = 1
    return

def main():
    ans = input_string()
    geez(ans)

if __name__ == "__main__":
    main()
