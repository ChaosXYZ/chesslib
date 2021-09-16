
class Tile: 
    
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.piece = None
       
    def getCoords(self):
        return (self.i, self.j)
    
    def hasPiece(self):
        if self.piece != None:
            return True
        return False
    
    def getPiece(self):
        return piece
       
    def setPiece(self, piece):
        self.piece = piece
    
    def removePiece(self):
        self.piece = None
        
    def __str__(self):
        if self.piece != None:
            return self.piece.getSymbol()
        return "  "
    
    def __repr__(self):
        if self.piece != None:
            return self.piece.getSymbol()
        return " "
        
        