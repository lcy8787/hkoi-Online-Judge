import math

ticket_price = input()

price = float(ticket_price[1:])

if 0.1 <= price <= 20.0:
    child_price = price / 2
    rounded_price = math.ceil(child_price * 10) / 10  # Round up to the nearest tenth
    formatted_price = '${:.1f}'.format(rounded_price)
    print(formatted_price)