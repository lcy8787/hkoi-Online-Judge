with open('account.txt', 'r') as file:
    N = int(file.readline().strip())
    balance = 0
    for i in range(N):
        transaction = int(file.readline().strip())
        balance += transaction
        
print(balance)