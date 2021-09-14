from BasePiece import Piece

class Bishop(Piece):
    def __init__(self, colour, i, j):
        if colour == 0:
            Piece.__init__(self, "♗", 0, i, j)
        else:
            Piece.__init__(self, "♝", 1, i, j)
        print("Bishop piece")