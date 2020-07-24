from player import player
from board import board
import os
import time


b=board(9)
b.setPieces(b.dimension)
def main():

  while bool:

    os.system('clear')
    b.BoardDisplay()
    I_FROM=input('\n' + 'From >>  ')
    if I_FROM==':q':
        break
    elif I_FROM==':s':
        print('save')
    I_TO=input('To     >>  ')
    p= player('white', b)
    p2= player('black', b)
    b.moves(I_FROM, I_TO)

    #print(b.board1)
    time.sleep(2)



if __name__ == '__main__':
            main()



