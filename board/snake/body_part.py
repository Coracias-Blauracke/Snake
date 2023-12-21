from board.board_object import BoardObject


class BodyPart(BoardObject):
    def __init__(self, x, y, type):
        super().__init__(x, y)
        self.type = type
    