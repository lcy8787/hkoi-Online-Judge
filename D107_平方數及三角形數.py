import math

def is_square_number(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

def is_triangular_number(n):
    x = (math.sqrt(8 * n + 1) - 1) / 2
    return x == int(x)

def check_number_type(n):
    is_square = is_square_number(n)
    is_triangular = is_triangular_number(n)

    if is_square and is_triangular:
        return "Both"
    elif is_square:
        return "Square"
    elif is_triangular:
        return "Triangular"
    else:
        return "Neither"

N = int(input())

result = check_number_type(N)
print(result)