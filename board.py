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
    #Place the white pieces on the board.
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
    #def setBlack(self, size):
    def setBlack(self, size):
        
        blackPawns=  (self.nbrPawns-1)*2//3 + 1
        #only for the black pawns on top and bottom without the middle ones
        count=0
        #size-3 +1 cause size-3 is not included.
        for i in range(4, size-3 +1):
            self.board1['a'+str(i)]= 'B'+ str(i-3)
            self.board1[self.yAxis[-1]+str(i)]='B'+ str( blackPawns - (i-3))
            count+=1
# size-4 cause yAxis[] start at index 0 but our letters start at 1
        cpt = 1
        for i in range( 3, size-4 + 1 ):
            self.board1[self.yAxis[i]+ '1' ]= 'B'+str( cpt +count)
            self.board1[self.yAxis[i]+str(size)]='B'+ str(blackPawns-count-cpt)
            cpt+=1
        #b5 for size 9
        self.board1[ self.yAxis[1]+ str( size//2 +1)] = 'B'+str(blackPawns//2-1)
        #h5 for s9
        self.board1[ self.yAxis[-2] + str(size//2+1) ] = 'B'+str(blackPawns//2)
        #e2 for s9
        self.board1[ self.yAxis[size//2] + '2' ] = 'B'+str(blackPawns//2+1)
        #e8 for s9
        self.board1[ self.yAxis[size//2] +str(size-1)]='B'+str(blackPawns//2+2)


    def setPieces(self, size):
        self.setWhite(size)
        self.setBlack(size)
    
    def moves(self, fromPos, toPos, player):
        
        if toPos in self.validMoves(fromPos):
            self.board1[toPos]=self.board1[fromPos]
            self.board1[fromPos]= "empty"
        else:
            print("Invalid move, you can't move diagonally or over other pawns")
            return False
        
        if self.board1[toPos][0] == 'K' :
            player.pawns['K'].changePos(toPos)

    
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
        if self.board1[pos][0] != 'K':
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
    def capture(self, pos):
        #right direction pos[1]+1 cause we don't want to test his actual position

        firstCase= self.board1[pos[0] +str(int(pos[1])+ 1)]
        scndCase= self.board1[pos[0]+ str(int(pos[1])+ 2 )]
        posLetter= self.board1[pos]
        
        
        if firstCase[0] != 'K' and posLetter[0] != firstCase[0] and \
           posLetter[0] == scndCase[0]:
            
            self.board1[pos[0]+str(int(pos[1])+1)]="empty"

        #left direction
        firstCase= self.board1[pos[0]+ str(int(pos[1])-1 )]
        scndCase= self.board1[pos[0]+str(int(pos[1])-2 )]
        
        if firstCase[0] != 'K' and posLetter[0] != firstCase[0] and \
           posLetter[0] == scndCase[0]:  
            
            self.board1[pos[0]+ str(int(pos[1])-1) ]= "empty"
        
        #top direction 
        #INDX to get the index of the letter cause pos contain "a1" or "f4"
        posLetterINDX= string.ascii_lowercase.index(pos[0])
        firstCase=self.board1[string.ascii_lowercase[posLetterINDX+1] + pos[1]]
        scndCase=self.board1[string.ascii_lowercase[posLetterINDX+2] + pos[1]]     
        
        if firstCase[0] != 'K' and  posLetter[0] != firstCase[0] and \
           posLetter[0] == scndCase[0]: 
            
            self.board1[string.ascii_lowercase[posLetterINDX+1]+ pos[1]]="empty"
        
        #bottom direction
        firstCase=self.board1[string.ascii_lowercase[posLetterINDX-1] + pos[1]]
        scndCase=self.board1[string.ascii_lowercase[posLetterINDX-2] + pos[1]]
       
        
        if firstCase[0] != 'K' and posLetter[0] != firstCase[0] and \
           posLetter[0] == scndCase[0]:
            
            self.board1[string.ascii_lowercase[posLetterINDX-1]+ pos[1]]="empty"
            
    def kinginCorners(self, player):
        kingPos= player.pawns['K'].getPos()
        bool= False
        if  kingPos in self.getCorners():
            return True

        return bool

    #Returns the numbers of pawns
    def getNbrPawns(self):
        return self.nbrPawns


    def BoardDisplay(self):
        #color_definition
        CLR_GOLD='\033[40m'
        CLR_DFLT='\033[00m'
        #print(CLR_GOLD + 'hello guys', CLR_DFLT)

        size=self.dimension
        line1=" |     "*size +"|"
        topline = "  " +( "______ "*size)
        for x in range(1,size+1):
            print(" |   " +str(x) ,end=" ")
         
        print("\n" + CLR_GOLD + topline,CLR_DFLT + "\n"+ CLR_GOLD + line1, CLR_DFLT)

        for x in self.board1:

            val=self.board1[x]
            if val=='empty':
                pawn='__'
            elif len(val)<2:
                pawn=val+" "

            else:
                if val[0]=='B':
                    pawn='B '
                elif val[0]=='W':
                    pawn='W '


        #DisplayingPawns
            if str(size) in x:
                print(CLR_GOLD + " |_"+pawn+"__" +"|" "\n"+line1, CLR_DFLT)
            else:
                if x[1]=='1':
                        print(CLR_GOLD + x[0].upper()+"|_"+pawn+"__", end="")
                else:
                        print(" |_"+pawn+"__", end="")


      

