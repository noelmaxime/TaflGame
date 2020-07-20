import string
from pawn import pawn
from board import board
class player:
    
    b = board(9) 
    if b.dimension == 9:
        nbrPawns= 25
    else:
        nbrPawns=37
    
    middle= (b.dimension)//2 + 1

    def __init__(self, color ):
        self.color = color
        pawns = {}
        self.pawns = pawns
        self.addPawns(self.nbrPawns)

    def addPawns(self ,Pawns):
        if self.color == 'white':
            self.pawns['K'] = pawn('white', 'King', 
                                   string.ascii_lowercase[self.middle],
                                   self.middle)
            for i in range(1 ,  (Pawns-1)//3 + 1):

                self.pawns['P' +str(i)] =  pawn('white', 'pawn', 0, 0) 
        
        else:
            #two third of the pawns are black
            for i in range(1 ,  (Pawns-1)*2//3 +1 ):
                self.pawns['P'+str(i)] =  pawn('black', 'Pawn', 0, 0)
    def getnbrPawns(self):
        return nbrPawns
