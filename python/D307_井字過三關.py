def check_winner(board):
    # 檢查垂直線
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '.':
            return board[0][col] + " wins"

    # 檢查橫線
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '.':
            return board[row][0] + " wins"

    # 檢查對角線
    if board[0][0] == board[1][1] == board[2][2] != '.':
        return board[0][0] + " wins"
    
    if board[0][2] == board[1][1] == board[2][0] != '.':
        return board[0][2] + " wins"
    
    # 檢查遊戲是否已結束
    for row in range(3):
        for col in range(3):
            if board[row][col] == '.':
                return "Not ended"

    # 遊戲已結束，沒有玩家勝出
    return "Draw"


# 讀取輸入的狀態
board = []
for _ in range(3):
    row = list(input())
    board.append(row)

# 判斷遊戲狀態
result = check_winner(board)

# 輸出結果
print(result)