class Piece:

    def __init__(self, symbol, colour, i, j):
        self.symbol = symbol
        self.colour = colour
        self.i = i
        self.j = j

    def getSymbol():
        return self.symbol

    def getColour():
        return self.colour

    def getCoords():
        return (self.i, self.j)

    def updateCoords(i, j):
        self.i = i
        self.j = j