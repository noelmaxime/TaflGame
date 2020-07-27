from player import player
from board import board
import os
import time

def main():
  b=board(9)
  b.setPieces(b.dimension)
  p= player('white', b)
  p2= player('black', b)
  turn = True
  gameContinue= True

  while gameContinue:
      os.system('clear')
      print(b.board1)
      b.BoardDisplay()
      if turn :
          current= p2
          turn = False
      else:
          current=p
          turn = True

      I_FROM=input('\n' + 'From >>  ')
      if I_FROM==':q':
          break
      elif I_FROM==':s':
          print('save')
      I_TO=input('To     >>  ')
      try:
          b.moves(I_FROM, I_TO, current)
      except:
          pass
      try:
          b.capture(I_TO)
      except:
          pass
      if current == p:
          if b.kinginCorners(p):
              gameContinue = False


      #print(b.board1)
      time.sleep(2)
  print("The Defenders won the game GG")


if __name__ == '__main__':
    main()



