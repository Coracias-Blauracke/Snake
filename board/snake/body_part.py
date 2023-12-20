from board.board_object import BoardObject


class BodyPart(BoardObject):
    def __init__(self, x, y, type):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.type = type
    