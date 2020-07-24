

#color_definition
CLR_GOLD='\033[40m'
CLR_DFLT='\033[00m'
#print(CLR_GOLD + 'hello guys', CLR_DFLT)


import string
size=self.dimension
line1=" |     "*size +"|"
topline = "  " +( "______ "*size) 

print(CLR_GOLD + topline+"\n"+line1, CLR_DFLT)

for x in board1:

    val=self.board1[x]
    if val=='empty':
        pawn='__'
    elif len(val)<2:
        pawn=val+" "
    
    else:
        if val[0]=='P':
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

for x in range(1,size+1):
    print(" |   " +str(x), end=" ") 
