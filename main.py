from player import player
from board import board

def main():
    b = board(9)
    p= player('white', b.nbrPawns)
    p2= player('black', b.nbrPawns)
    b.setPieces(b.dimension)
    print(p.pawns)
#    print(b.board1)
    b.moves('c5','c3', p)
    b.moves('d5', 'd4',p)
    b.moves('e5','c5', p)
    b.moves('c5','c9', p)
    b.moves('c9','a9', p)
    print(b.board1)
    b.capture('d5')
#    print(b.board1)
#    b.moves('e5', 'c5')
#    b.moves('f5', 'd5')
#    print(b.board1)
#    b.moves('c9','a9')
    
#    print(b.board1)
    print(b.nbrPawns)
if __name__ == '__main__':
    main()
#bool = True
#while
#if bool :
#     current= P1
#     bool = False
#else:
#     bool=True
#     current=P2

