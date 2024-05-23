def get_ordinal_suffix(number):
    last_two_digits = number % 100
    if 11 <= last_two_digits <= 13:
        return "th"

    last_digit = number % 10
    if last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"

N = int(input())

if not 1 <= N <= 9999:
    pass
else:
    suffix = get_ordinal_suffix(N)
    ordinal_number = str(N) + suffix
    print(ordinal_number)