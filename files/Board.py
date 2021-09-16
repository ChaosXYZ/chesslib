from Tiles import Tile
from Pieces import *

class Board:

    def __init__(self, FEN = None):
        self.turn = 0
        self.movenum = 0
        self.board = []
        self.enpassant = "-"
        #castling availability = [WhiteKingside, WhiteQueenside,
        #                       BlackKingside, BlackQueenside]
        self.castling = [True, True, True, True]
        
        for i in range(8):
            row = []
            for j in range(8):
                row.append(Tile(i,j))
            self.board.append(row)
        if FEN == None:
            self.initialize()


    def initialize(self):
        self.board[0][0].setPiece(Rook(1))
        self.board[0][1].setPiece(Knight(1))
        self.board[0][2].setPiece(Bishop(1))
        self.board[0][3].setPiece(Queen(1))
        self.board[0][4].setPiece(King(1))
        self.board[0][5].setPiece(Bishop(1))
        self.board[0][6].setPiece(Knight(1))
        self.board[0][7].setPiece(Rook(1))

        for i in range(8):
            self.board[1][i].setPiece(Pawn(1))

        self.board[7][0].setPiece(Rook(0))
        self.board[7][1].setPiece(Knight(0))
        self.board[7][2].setPiece(Bishop(0))
        self.board[7][3].setPiece(Queen(0))
        self.board[7][4].setPiece(King(0))
        self.board[7][5].setPiece(Bishop(0))
        self.board[7][6].setPiece(Knight(0))
        self.board[7][7].setPiece(Rook(0))

        for i in range(8):
            self.board[6][i].setPiece(Pawn(0))

    def display(self):
        for i in range(8):
            print("{a} ".format(a=8-i), end="|")
            for j in range(8):
                print(self.board[i][j],end="|")
            print("\n")

    def FENstats(self):
        cols = ["White","Black"]
        print("To move: " + cols[self.turn])
        print("Moves passed: ", self.movenum)
        print("White Kingside Castle: ", self.castling[0])
        print("White Queenside Castle: ", self.castling[1])
        print("Black Kingside Castle: ", self.castling[2])
        print("Black Queenside Castle: ", self.castling[3])
        print("En passant moves: " + self.enpassant)

    def importFEN(self, FEN):
        #'rnbqkbnr/pp1ppppp//8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'
        fen = 'rnbqkbnr/pp1ppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'.split(' ')
        self.enpassant = fen[3]
        self.turn = 1 if fen[1] == "b" else 0
        self.movenum = fen[5]

        #Castling array
        for i in fen[2]:
            if i == "K":
                self.castling[0] = True
            if i == "Q":
                self.castling[1] = True
            if i == "k":
                self.castling[2] = True
            if i == "q":
                self.castling[3] = True

        #setting up the board
        boardconfig = fen[0].split("/")
        for i in range(8):
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
            j = 0
            while j != 8:
                if boardconfig[i][j] in num:
                    j += int(boardconfig[i][j])
                
