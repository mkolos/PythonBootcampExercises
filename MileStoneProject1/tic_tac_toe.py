import random


def display_board(board):
    print('\n' * 100)
    for row in range(1, 12):
        print(get_lines(row, board))


def get_lines(row, board):
    rows = {
        1: '   |   |   ',
        2: ' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ',
        3: '   |   |   ',
        4: '-' * 12,
        5: '   |   |   ',
        6: ' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ',
        7: '   |   |   ',
        8: '-' * 12,
        9: '   |   |   ',
        10: ' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ',
        11: '   |   |   ',
    }

    return rows[row]


def player_input():
    player_one = ''

    while player_one != 'X' and player_one != 'O':
        player_one = input('Player 1: Do you want to be X or O? ').upper()

    if player_one == 'X':
        return {'X': 'Player One', 'O': 'Player Two'}
    else:
        return {'O': 'Player One', 'X': 'Player Two'}


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))


def choose_first():
    return 'X' if random.randint(0, 1) == 1 else 'O'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for position in range(1, 10):
        if space_check(board, position):
            return False

    return True


def player_choice(board, marker):
    choice = 0
    while choice not in range(1, 10) or not space_check(board, choice):
        choice = int(input('Please place your {} with numpad (1-9) '.format(marker)))

    return choice


def replay():
    answer = ''
    while answer != 'yes' and answer != 'no':
        answer = input('Do you want to play again? /yes or no/')
        answer = answer.lower()

    return True if answer == 'yes' else False


def get_base_board():
    return [' '] * 10


def change_marker(marker):
    return 'X' if marker == 'O' else 'O'


def play_game():
    print('Welcome to Tic Tac Toe!')

    game_is_running = True
    while game_is_running:
        players = player_input()
        marker = choose_first()
        board = get_base_board()
        display_board(board)
        print('Start game with {}'.format(players[marker]))
        is_win = False
        is_full = False
        while not is_win and not is_full:
            position = player_choice(board, marker)
            place_marker(board, marker, position)
            is_win = win_check(board, marker)
            is_full = full_board_check(board)
            display_board(board)
            if not is_win and not is_full:
                marker = change_marker(marker)

        if is_full:
            print("It's draw!")
        elif is_win:
            print('Congratulation for the {}. You won the game'.format(players[marker]))

        game_is_running = replay()

    print('Thanks for the game. Come back soon ;)')


play_game()
