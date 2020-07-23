from player import player
from board import board

def main():
    b = board(9)
    p= player('white', b)
    p2= player('black', b)
    b.setPieces(b.dimension)
    print(b.board1)
    b.moves('d5', 'd4')
    b.moves('c5','c4')
    
#    print(b.board1)
    b.moves('e5', 'c5')
    b.moves('f5', 'd5')
    print(b.board1)
#    b.moves('c9','a9')
    
#    print(b.board1)
    print(b.nbrPawns)
if __name__ == '__main__':
    main()
