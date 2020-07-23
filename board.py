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
        self.middle = dimension//2+1
        self.midLetter= string.ascii_lowercase[self.middle-1]
        #to have lowercase letters on the y axis.
        yAxis= string.ascii_lowercase[:dimension]
        self.yAxis= yAxis
        
        for i in yAxis:
            for j in range(1, dimension+1):
                board1[i+str(j)]='empty' 
    
    def setWhite(self, size):
        cpt=1
        for i in range(self.middle-2, self.middle+2 +1):
            if (i== self.middle):
                continue
            self.board1[self.midLetter+ str(i)] = 'W' +str(cpt)
            cpt+=1
        for i in string.ascii_lowercase[self.middle-3:self.middle+2]:
            if (i == 'e'):
                continue
            self.board1[i+ str(self.middle)]= 'W'+ str(cpt)
            cpt+=1
        self.board1[self.midLetter + str(self.middle)]= 'K'
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
            self.board1[self.yAxis[i]+str(size)]='P'+ str(blackPawns-count-cpt)
            cpt+=1
         #b5 for S9
        self.board1[ 'b'+ str( size//2 +1)] = 'P'+str(blackPawns//2-1)
        #h5 for size 9
        self.board1[ self.yAxis[-2] + str(size//2+1) ] = 'P'+str(blackPawns//2)
        #e2 for S9
        self.board1[ self.yAxis[size//2] + '2' ] = 'P'+str(blackPawns//2+1)
        #e8 for S9
        self.board1[ self.yAxis[size//2] +str(size-1)]='P'+str(blackPawns//2+2)


    def setPieces(self, size):
        self.setWhite(size)
        self.setBlack(size)
    
    def moves(self, fromPos, toPos):
        
        if toPos in self.validMoves(fromPos):
            self.board1[toPos]=self.board1[fromPos]
            self.board1[fromPos]= "empty"
            
        else:
            print("Invalid move, you can't move diagonally or over other pawns")
    
    def validMoves(self , pos):
        moves = []
        #right direction pos[1]+1 cause we don't want to test his actual position
        for i in range(int(pos[1])+ 1, self.dimension+1 ):
            if self.board1[ pos[0] + str(i) ] != "empty":
                break
            else:
                moves.append(pos[0] + str(i))
        #left direction
        for i in range(int(pos[1])-1, 0, -1):
            if self.board1[ pos[0]+ str(i) ] != "empty":
                break
            else:
                moves.append(pos[0] + str(i))
        #top direction
        posLetterINDX= string.ascii_lowercase.index(pos[0])
        for i in string.ascii_lowercase[posLetterINDX+1:self.dimension]:
            if self.board1[i + pos[1]] != "empty":
                break
            else:
                moves.append(i + pos[1] )
        #bottom direction
        for i in range(posLetterINDX, 0, -1):
            letter= string.ascii_lowercase[i-1]
            if self.board1[letter + pos[1]] !="empty":
                break
            else:
                moves.append(letter +pos[1] )
        #Remove the corners and the throne for the valid moves if not the king.
        if self.board1[pos] != 'K':
            for i in self.getCorners():
                if i in moves:
                    moves.remove(i)
            thronePos=self.midLetter + str(self.middle)
            if thronePos in moves:
                moves.remove(thronePos)


        
        print("List of valid moves : ", moves )    
           
        return moves     
    #Return a list of the corners of the board
    def getCorners(self):
        cornerList=["a1"]
        downRightCorn= "a" + str(self.dimension)
        upLeftCorn= string.ascii_lowercase[self.dimension-1]  + "1"
        upRightCorn= string.ascii_lowercase[self.dimension-1]+ str(self.dimension)
        cornerList.extend((downRightCorn, upLeftCorn, upRightCorn))
        return cornerList
    
    #Returns the numbers of pawns
    def getNbrPawns(self):
        return self.nbrPawns



