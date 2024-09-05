tea = int(input())
ice = input()
sweet = input()
price = 0

if tea >= 1 and tea <= 10:
    if tea in [1, 2, 3]:
        price += 15
    elif tea in [4, 5, 6]:
        price += 18
    elif tea in [7, 8]:
        price += 20
    elif tea in [9, 10]:
        price += 30

if ice == "No Ice":
    price += 3
elif ice == "Less Ice":
    price += 2

if sweet == "0%":
    price += 4
elif sweet == "30%":
    price += 2
elif sweet == "50%":
    price += 1

toppings_price = {
    "Pearl": 4, "Pudding": 4, "Aloe": 5, "Agar": 5,
    "Grass Jelly": 6, "Lychee Jelly": 6, "Coffee Jelly": 6,
    "Red Beans": 7, "Crystal Jelly Ball": 7
}

num_toppings = int(input())

if num_toppings > 0:
    toppings = input().split(", ")
    unique_toppings = set(toppings)
    for topping in unique_toppings:
        if topping in toppings_price:
            price += toppings_price[topping]

print(price)