board = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " "
]
wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 4, 8],
    [2, 4, 6],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8]
]
def print_board():
    split = 3
    index = 0
    output = "|"
    while index < len(board):
        output += board[index] + "|"
        if (index + 1) % 3 == 0:
            print(output)
            output = "|"
        index += 1

def move(move: str, r: int, c: int):
    board[c+3*r] = move
    return
def test_win(char: str) -> bool:
    won = False
    for cond in wins:
        if (board[cond[0]] == board[cond[1]] == board[cond[2]]) and  \
            (board[cond[0]] != " " and board[cond[1]] != " " and board[cond[2]] != " "):
            won = True
    return won
def game():
    cur = "X"
    cont = True
    while cont:
        decision = input(f"Where to put {cur}? (row column): ")
        [r, c] = decision.split(" ")
        move(cur, int(r)-1, int(c)-1)
        won = test_win(cur)
        print_board()
        if won:
            print(f"{cur} won!")
            return
        cur = "O" if cur == "X" else "X"
game()