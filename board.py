import string
from pawn import pawn
class board:
    def __init__(self, dimension ):
        self.dimension= dimension
        #board is an empty dictionary
        board1 = {}
        
        self.board1= board1
        if dimension == 9:
             nbrPawns= 25
        else:
             nbrPawns=37
        self.nbrPawns= nbrPawns
        #to have lowercase letters on the y axis.
        yAxis= string.ascii_lowercase[:dimension]
        self.yAxis= yAxis
        
        for i in yAxis:
            for j in range(1, dimension+1):
                board1[i+str(j)]='empty' 
    
    def setWhite(self, size):
        middle= size//2 + 1
        midLetter= string.ascii_lowercase[middle-1]
        cpt=1
        for i in range(middle-2, middle+2 +1):
            if (i== middle):
                continue
            self.board1[midLetter+ str(i)] = 'W' +str(cpt)
            cpt+=1
        for i in string.ascii_lowercase[middle-3:middle+2]:
            if (i == 'e'):
                continue
            self.board1[i+ str(middle)]= 'W'+ str(cpt)
            cpt+=1
        self.board1[midLetter + str(middle)]= 'K'
    def setBlack(self, size):
        blackPawns=  (self.nbrPawns-1)*2//3 + 1
        #only for the black pawns on top and bottom without the middle ones
        count=0
        #size-3 +1 cause size-3 is not included.
        for i in range(4, size-3 +1):
            self.board1['a'+str(i)]= 'P'+ str(i-3)
            self.board1[self.yAxis[-1]+str(i)]='P'+ str( blackPawns - (i-3))
            count+=1
 # previous  for i in range(self.yAxis[3], self.yAxis[size-4] ):
         # size-4 cause yAxis[] start at index 0 but our letters start at 1
        cpt = 1
        for i in range( 3, size-4 + 1 ):

            self.board1[self.yAxis[i]+ '1' ]= 'P'+str( cpt +count)
            self.board1[self.yAxis[i]+ str(size)]= 'P'+ str(blackPawns-count -cpt )
            cpt+=1
         #b5 for S9
        self.board1[ 'b'+ str( size//2 +1)] = 'P'+str(blackPawns//2-1)
        #h5 for size 9
        self.board1[ self.yAxis[-2] + str(size//2+1) ] = 'P'+str(blackPawns//2)
        #e2 for S9
        self.board1[ self.yAxis[size//2] + '2' ] = 'P'+str(blackPawns//2+1)
        #e8 for S9
        self.board1[ self.yAxis[size//2] + str(size-1) ] = 'P'+str(blackPawns//2+2)


    def setPieces(self, size):
        self.setWhite(size)
        self.setBlack(size)
    

