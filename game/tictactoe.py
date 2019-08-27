from random import choice, random
#ask to user to play again
def playAgain():
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

def check_winner(board, letter):
    flag = False
    for [i, j, k] in winOptions:
        flag = flag or (board[i] == letter and board[j] == letter and board[k] == letter)
    return flag

def make_move(board, letter, move):
    board[move] = letter

def check_space_free(board, move):
    return board[move] == ' '

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

def get_random_move(board, movesList):
    availableMoves = []
    for i in movesList:
        if check_space_free(board, i):
            availableMoves.append(i)

    if len(availableMoves) != 0:
        return choice(availableMoves)
    else:
        return None

def get_computer_move(board, computer):
    # check center
    if check_space_free(board, 4):
        return 4
    # try win
    for i in range(9):
        copy = list(board)
        if check_space_free(copy, i):
            make_move(copy, computer, i)
            if check_winner(copy, computer):
                return i

    # block player
    for i in range(9):
        copy = list(board)
        if check_space_free(copy, i):
            make_move(copy, player, i)
            if check_winner(copy, player):
                return i
    # check corners
    move = get_random_move(board, [0, 2, 6, 8])
    if move != None:
        return move

    # retutn sides
    return get_random_move(board, [1, 3, 5, 7])

#define the options with which you can win
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
player = 'O'
computer = 'X'


def start_game(theBoard):
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
                # computer
                move = get_computer_move(theBoard, computer)
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

        if not playAgain():
            break

def main():
    theBoard = [' '] * 9
    start_game(theBoard)

if __name__ == "__main__":
    main()