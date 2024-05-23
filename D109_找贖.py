def withdraw(amount):
    denominations = [1000, 500, 100, 50, 20, 10]
    result = []
    
    for denomination in denominations:
        count = amount // denomination
        amount %= denomination
        result.extend([denomination] * count)
    
    return result

amount = int(input())

result = withdraw(amount)

for note in result:
    print(note)