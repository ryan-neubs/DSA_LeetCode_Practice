def isValidSudoku(board):
    rows = [set() for x in range(9)]
    cols = [set() for x in range(9)]
    secs = [set() for x in range(9)]
    for row in range(9):
        for col in range(9):
            curr_val = board[row][col]
            if curr_val == '.': 
                continue

            if curr_val in rows[row]: 
                return False
            rows[row].add(curr_val)

            if curr_val in cols[col]: 
                return False
            cols[col].add(curr_val)
            
            curr_sec = (row//3) * 3 + (col//3) # Calculate the section index
            if curr_val in secs[curr_sec]:
                return False
            secs[curr_sec].add(curr_val)
            
    return True

board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","9",".","6"],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))
            