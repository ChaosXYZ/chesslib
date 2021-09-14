from BasePiece import Piece

class Pawn(Piece):
    def __init__(self, colour):
        if colour == 0:
            Piece.__init__(self, "♙", 0)
        else:
            Piece.__init__(self, "♟", 1)
