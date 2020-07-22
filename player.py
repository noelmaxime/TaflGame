import string
from pawn import pawn
from board import board
class player:
    
#    b = board(9) 
#    if b.dimension == 9:
#        nbrPawns= 25
#    else:
#        nbrPawns=37
    
 #   middle= (b.dimension)//2 + 1

    def __init__(self, color, board ):
        self.color = color
        pawns = {}
        self.pawns = pawns
        self.addPawns(board.getNbrPawns())

    def addPawns(self , NbrPawns):
        if self.color == 'white':
            self.pawns['K'] = pawn('white', 'King', 0, 0)
            for i in range(1 , (NbrPawns -1)//3 + 1):

                self.pawns['P' +str(i)] = pawn('white', 'pawn', 0, 0) 
        
        else:
            #two third of the pawns are black
            for i in range(1 , (NbrPawns -1)*2//3 +1 ):
                self.pawns['P'+str(i)] = pawn('black', 'Pawn', 0, 0)
    
