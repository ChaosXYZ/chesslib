class Piece:

    def __init__(self, symbol, colour, i, j):
        self.symbol = symbol
        self.colour = colour
        self.i = i
        self.j = j

    def getSymbol(self):
        return self.symbol

    def getColour(self):
        return self.colour

    def getCoords(self):
        return (self.i, self.j)

    def updateCoords(self,i, j):
        self.i = i
        self.j = j