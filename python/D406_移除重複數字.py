def unique_numbers():
    N = int(input())
    numbers = list(map(int, input().split()))
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    print(len(unique_numbers))
    print(' '.join(map(str, unique_numbers)))

unique_numbers()
