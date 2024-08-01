def tictactoe(moves):
    print("Welcome to Tic Tac Toe!")
    board = [["-" for _ in range(3)] for _ in range(3)]
    print("Here's the current board:")
    
    for move in moves:
        row, col = move
        if moves.index(move) % 2 == 0:
            board[row][col] = "A"
        else:
            board[row][col] = "B"

    if board[0][0] == board[1][1] == board[2][2]!= "-":
            return(board[0][0] + " wins!")
    if board[0][2] == board[1][1] == board[2][0]!= "-":
            return(board[0,2] + " wins!")
    for i in range(3):
        
        if board[i][0] == board[i][1] == board[i][2]!= "-":
            return(board[i][0] + " wins!")
        elif board[0][i] == board[1][i] == board[2][i]!= "-":
            return(board[0][i] + " wins!")
    if any('-' in sublist for sublist in board):
        return "Game in progress"
    else:
        return "It's a draw!"
    
result = tictactoe([[0,0],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
print(result)

