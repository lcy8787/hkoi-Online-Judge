def algebraic_to_coordinates(algebraic):
    column = ord(algebraic[0]) - ord('a')
    row = int(algebraic[1]) - 1
    return row, column

def king_moves(start, end):
    start_row, start_column = algebraic_to_coordinates(start)
    end_row, end_column = algebraic_to_coordinates(end)

    row_distance = abs(end_row - start_row)
    column_distance = abs(end_column - start_column)

    max_distance = max(row_distance, column_distance)
    return max_distance

start = input()
end = input()
minimum_moves = king_moves(start, end)
print(minimum_moves)