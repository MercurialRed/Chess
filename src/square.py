class Square:

    def __init__(self, row, col, piece=None):  # a square may contain a piece or not
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != None
        
