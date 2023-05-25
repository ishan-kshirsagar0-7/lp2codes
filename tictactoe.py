def ConstBoard(board):
    print("Current State Of Board:\n")
    for i in range(0, 9):
        print("- " if board[i] == 0 else "O " if board[i] == 1 else "X ", end=" " if i % 3 < 2 else "\n")
    print("\n")

def UserTurn(board):
    pos = int(input("Enter X's position from [1...9]: "))
    if board[pos-1] != 0:
        print("Wrong Move!!!")
        exit(0)
    board[pos-1] = -1

def a_star(board, player):
    x = analyzeboard(board)
    if x != 0:
        return x * player
    pos, value = -1, -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -a_star(board, player*-1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    return 0 if pos == -1 else value

def CompTurn(board):
    pos, value = -1, -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -a_star(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1

def analyzeboard(board):
    cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0, 8):
        if board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] == board[cb[i][2]]:
            return board[cb[i][2]]
    return 0

def main():
    board = [0] * 9
    print("Computer: O Vs. You: X")
    player = int(input("Enter to play 1(st) or 2(nd): "))
    for i in range(0, 9):
        if analyzeboard(board) != 0:
            break
        if (i + player) % 2 == 0:
            CompTurn(board)
        else:
            ConstBoard(board)
            UserTurn(board)
    x = analyzeboard(board)
    ConstBoard(board)
    print("DRAW !" if x == 0 else "YOU WON !" if x == -1 else "YOU LOST !")

main()