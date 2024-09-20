def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    #Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  #Winner in a row
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  #Winner in a column

    #Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  #Winner in the main diagonal
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  #Winner in the other diagonal

    return None  #No winner

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False  #There's an empty space, board is not full
    return True  #Board is full

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie! The board is full.")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. The space is already taken. Try again!")

if __name__ == "__main__":
    tic_tac_toe()
