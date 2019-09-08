def play_again():
    print('Replay? (yes or no)')
    return input().lower().startswith('y')

def show_board(tablero):
    print('______________')
    print('     |     |')
    print('1 ' + tablero[0] + '  |2 ' + tablero[1] + '  |3' + tablero[2])
    print('     |     |')
    print('______________')
    print('     |     |')
    print('4  ' + tablero[3] + ' |5 ' + tablero[4] + '  |6' + tablero[5])
    print('     |     |')
    print('______________')
    print('     |     |')
    print('7  ' + tablero[6] + ' |8 ' + tablero[7] + '  |9 ' + tablero[8])
    print('     |     |')
    print('______________')

def game_over(board):
    return check_winner(board, player) or check_winner(board, computer)

def check_winner(board, letter):
    winOptions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [6, 4, 2],
    ];
    flag = False
    for [i, j, k] in winOptions:
        flag = flag or (board[i] == letter and board[j] == letter and board[k] == letter)
    return flag


def make_move(board, letter, move):
    board[move] = letter


def check_space_free(board, move):
    return board[move] == ' '


def get_free_spaces(board):
    emptySpaces = []
    for i in range(9):
        if board[i] == ' ':
            emptySpaces.append(i)
    return emptySpaces


def get_player_move(board):
    move = ' '
    print('What is your next move? (1-9)')
    move = input()

    while not move.isdigit():
        print('What is your next move? (1-9)')
        move = input()

    return int(move) - 1

def check_board_full(board):
    for i in range(9):
        if check_space_free(board, i):
            return False
    return True

def evaluate(board):
    if check_winner(board, computer):
        score = +1
    elif check_winner(board, player):
        score = -1
    else:
        score = 0
    return score

def minimax(board, depth, playerTurn):
    if playerTurn == computer:
        best = [-1, -1]
    else:
        best = [-1, 1]

    if game_over(board) or depth == 0:
        score = evaluate(board)
        return [-1, score]

    for availableMove in get_free_spaces(board):
        x = availableMove
        board[x] = playerTurn
        if playerTurn == computer:
            score = minimax(board, depth - 1, player)
        else:
            score = minimax(board, depth - 1, computer)
        board[x] = ' '
        score[0] = x

        if playerTurn == computer:
            if score[1] > best[1]:
                best = score
        else:
            if score[1] < best[1]:
                best = score

    return best

def get_computer_move(board):
    depth = len(get_free_spaces(board))
    move = minimax(board, depth, computer)
    return move[0]


player = 'O'
computer = 'X'
def start_game():
    theBoard = [' '] * 9
    while True:
        turn = 'player'
        playing = True
        while playing:
            if turn == 'player':
                # player
                show_board(theBoard)
                move = get_player_move(theBoard)
                make_move(theBoard, player, move)

                if check_winner(theBoard, player):
                    show_board(theBoard)
                    print('You are the winner!')
                    playing = False
                else:
                    if check_board_full(theBoard):
                        show_board(theBoard)
                        print('Tie Game!')
                        break
                    else:
                        turn = 'computer'
            else:
                move = get_computer_move(theBoard)
                make_move(theBoard, computer, move)

                if check_winner(theBoard, computer):
                    show_board(theBoard)
                    print('You lose the game.')
                    playing = False
                else:
                    if check_board_full(theBoard):
                        show_board(theBoard)
                        print('The game is a tie!')
                        playing = False
                        break
                    else:
                        turn = 'player'

        if not play_again():
            break
        else:
            theBoard = [' '] * 9


def main():
    start_game()

if __name__ == "__main__":
    main()