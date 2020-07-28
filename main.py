board = [' ' for x in range(10)]

# bo - board, le - letter, pos - position

def display_board(bo):
    print('   |   |')
    print(' ' + bo[1] + ' | ' + bo[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bo[4] + ' | ' + bo[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bo[7] + ' | ' + bo[8] + ' | ' + bo[9])
    print('   |   |')

def insert_in_board(le, pos):
    board[pos] = le

def is_space_free(pos):
    return board[pos] == ' '


def is_winner(bo, le):
    return ((bo[1] == bo[2] == bo[3] == le) or (bo[4] == bo[5] == bo[6] == le) or (bo[7] == bo[8] == bo[9] == le) or (bo[1] == bo[4] == bo[7] == le) or (bo[2] == bo[5] == bo[8] == le) or (bo[3] == bo[6] == bo[9] == le) or (bo[1] == bo[5] == bo[9] == le) or (bo[3] == bo[5] == bo[7] == le))


def is_board_full(bo):
    if bo.count(' ') > 1:
        return False
    else:
        return True


def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for le in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = le
            if is_winner(board_copy, le):
                move = i 
                return move

    open_corners = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    if len(open_corners) > 0:
        move = select_random(open_corners)
        return move

    if 5 in possible_moves:
        move = 5 
        return move

    open_edges = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            open_edges.append(i)
    if len(open_edges) > 0:
        move = select_random(open_edges)
    
    return move




def player_move():
    run = True
    while run:
        pos = input("Choose a position between 1-9: ")
        try:
            pos = int(pos)
            if pos > 0 and pos < 10:
                if is_space_free(pos):
                    run = False
                    insert_in_board('X', pos)
                else:
                    print("That position is already occupied.")
            else:
                print("Please select a number within the range.")
        except:
            print("Please input a valid number.")


def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main():
    print("Tic-Tac-Toe")
    print("\n")
    display_board(board)

    while not is_board_full(board):
        if not is_winner(board, 'O'):
            player_move()
            display_board(board)
        else:
            print("Computer won. Better luck next time.")
            break

        if not is_winner(board, 'X'):
            move = comp_move()
            if move == 0:
                break
            else:
                insert_in_board('O', move)
                print(f"Computer placed an X at position {move}:")
                display_board(board)
        else:
            print("You won. Well played.")
            break

    if is_board_full(board):
        print("It's a tie. No more spaces left to move.")


while True:
    choice = input("Wanna go again? (y/n) ")
    if choice.lower() == 'y' or choice.lower() =='yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break