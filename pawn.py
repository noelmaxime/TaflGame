
class pawn:
    def __init__(self, color, rank, y, x):
        self.color= color
        self.rank= rank
        self.x= x
        self.y= y

    def changePos(self, pos):
        self.y = pos[0]
        self.x = pos[1]
    
    def getPos(self):
        return self.y + self.x

