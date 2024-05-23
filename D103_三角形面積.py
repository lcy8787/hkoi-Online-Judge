import math
a = int(input())
b = int(input())
C = int(input())

C_rad = math.radians(C)

area = 0.5 * a * b * math.sin(C_rad)

formatted_area = "{:.3f}".format(area)

print(formatted_area)