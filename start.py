if move == -1:

# If player can win, block him.

for i in range(1,10):

if make_move(board, player, i, True)[1]:

move=i

break

if move == -1:

# Otherwise, try to take one of desired places.

for tup in moves:

for mv in tup:

if move == -1 and can_move(board, computer, mv):

move=mv

break

return make_move(board, computer, move)

def space_exist():

return board.count('X') + board.count('O') != 9

player, computer = select_char()

print('Player is [%s] and computer is [%s]' % (player, computer))

result='%%% Deuce ! %%%'

while space_exist():

print_board()

print('#Make your move ! [1-9] : ', end='')

move = int(input())

moved, won = make_move(board, player, move)

if not moved:

print(' >> Invalid number ! Try again !')

continue

if won:

result='*** Congratulations ! You won ! ***'

break

elif computer_move()[1]:

result='=== You lose ! =='

break;

print_board()

print(result)
