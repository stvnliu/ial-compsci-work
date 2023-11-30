board = [
    [
        " ", " ", " "
    ], [
        " ", " ", " "
    ], [
        " ", " ", " "
    ]
]
wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 4, 8],
    [2, 4, 6],
]
def print_board():
    for row in board:
        print("|"+ "|".join(row)+"|")
print_board() 
def move(move: str, r: int, c: int):
    board[r][c] = move
    return
def test_win(char: str) -> bool:
    won = True
    for cond in wins:
        if board[cond[0]] != board[cond[1]] != board[cond[2]]:
            won = False
    return won
def game():
    cur = "X"
    cont = True
    while cont:
        print_board()
        decision = input(f"Where to put {cur}? : ")
        [r, c] = decision.split(" ")
        move(cur, int(r), int(c))
        won = test_win(cur)
        if won:
            print(f"{cur} won!")
            return
        cur = "O" if cur == "X" else "X"
game()