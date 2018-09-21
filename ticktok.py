def display_borad(board):
    print(board[7] +'|'+ board[8] +'|'+ board[9])
    print(board[4] +'|'+ board[5] +'|'+ board[6])
    print(board[1] +'|'+ board[2] +'|'+ board[3])



def intake():    
    inlet1 = (input('Player1 enter your option X or O: ')).upper()
    if inlet1 == 'X':
        return ('X','O')
    else:
        return ('O','X')

def solution():    
    ans = [(1,2,3),(4,5,6),(7,8,9),(1,5,9),(7,5,3),(1,4,7),(2,4,6),(3,6,9)]
    for i in ans:
        if (test_board[i[0]] == test_board[i[1]] == test_board[i[2]] == 'X') or (test_board[i[0]] == test_board[i[1]] == test_board[i[2]] == 'O'):
               return print('you won the game-congradz')



    
    
a1 = intake()
    
test_board = ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

n = 1
while n <= 9:
        if n%2 != 0:
            z = int(input('Player1 please choose your number from 1 to 9: '))
            test_board[z] = a1[0]
            n += 1
            display_borad(test_board)
            solution()
    
        elif n%2 == 0:
            z = int(input('Player2 please choose your number from 1 to 9: '))
            test_board[z] = a1[1]
            n += 1
            display_borad(test_board)
            solution()
        