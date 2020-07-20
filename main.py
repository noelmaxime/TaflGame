from player import player

def main():
    p= player('white')
    p2= player('black')
    player.b.setPieces(player.b.dimension)
    
    print(player.b.board1)
    print(player.nbrPawns)
if __name__ == '__main__':
    main()
