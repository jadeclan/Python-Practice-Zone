
def transpose(board: list) -> list:
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

def check_rows(board) -> int:
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]
    return 0

def check_columns(board) -> int:
    transposed = transpose(board)
    return check_rows(transposed)

def check_diagonals(board) -> int:
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    return 0

def tic_tac_toe_winner(board) -> int:

    winner = check_rows(board)
    if winner != 0: return winner
    winner = check_columns(board)
    if winner != 0: return winner
    return check_diagonals(board)


def main():
    board = [[1, 0, -1],[0, -1, 0],[-1, -1, 1]]
    print(tic_tac_toe_winner(board))

main()