the_board = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '}
board_keys = []
for key in the_board:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '│' + board['8'] + '│' + board['9'])
    print('-+-+-')
    print(board['4'] + '│' + board['5'] + '│' + board['6'])
    print('-+-+-')
    print(board['1'] + '│' + board['2'] + '│' + board['3'])

def game():
    turn = 'X'
    count = 0
    for i in range 11:
        printBoard(the_board)
        print('its your turn'+turn+'move to which place?')
        move = input()
        if the_board[move] == ' ':
            the_board[move]= turn
            count += 1
        else:
            print('that place is already filled. Move to the next place')
            continue
            
        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                printBoard(the_board())
                print('GAME OVER!')
                print(turn+'won')
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                printBoard(the_board())
                print('GAME OVER!')
                print(turn+'won')
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                printBoard(the_board())
                print('GAME OVER!')
                print(turn+'won')
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                printBoard(the_board())
                print('GAME OVER!')
                print(turn+'won')
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                printBoard(the_board())
                print('GAME OVER!')
                print(turn+'won')
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                printBoard(the_board())
                print('GAME OVER!')
                print(turn+'won')
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':
                printBoard(the_board())
                print('GAME OVER!')
                print(turn+'won')
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                printBoard(the_board())
                print('GAME OVER!')
                print(turn+'won')
                break
        if count == 9:
            print('GAME OVER!')
            print('its a tie')
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input('do you want to play again? (y/n)')
    if restart == 'y':
        for  key in board_keys:
            the_board[key] = ' '

        game()

if __name__ == '__main__':
    game()