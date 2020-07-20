import string
from pawn import pawn
class board:
    def __init__(self, dimension ):
        self.dimension= dimension
        board1 = {}
        
        self.board1= board1
        if dimension == 9:
             nbrPawns= 25
        else:
             nbrPawns=37
        self.nbrPawns= nbrPawns
        yAxis= string.ascii_lowercase[:dimension]
        self.yAxis= yAxis
        for i in yAxis:
            for j in range(1, dimension+1):
                board1[i+str(j)]='empty' 
    
    def setPieces(self, size):
        blackPawns=  (self.nbrPawns-1)*2//3 + 1
        #only for the black pawns on top and bottom without the middle ones
        count=0
        for i in range(4, size-3):
            self.board1['a'+str(i)]= 'P'+ str(i-3)
            self.board1[self.yAxis[-1]+str(i)]='P'+ str( blackPawns - (i-3)) 
            count+=1 
#        for i in range(self.yAxis[3], self.yAxis[size-4] ):
        for i in range( 3, size-4 ):
            cpt=1
            self.board1[self.yAxis[i]+ '1' ]= 'P'+str( cpt +count)
            self.board1[self.yAxis[i]+ str(size)]= 'P'+ str(blackPawns-count -cpt )
            cpt+=1

        self.board1[ 'b'+ str( size//2 +1)] = 'P'+str(blackPawns//2-1)
        self.board1[ self.yAxis[-2] + str(size//2+1) ] = 'P'+str(blackPawns//2)
        self.board1[ self.yAxis[size//2] + '1' ] = 'P'+str(blackPawns//2+1)
        self.board1[ self.yAxis[size//2] + str(size-1) ] = 'P'+str(blackPawns//2+2)
