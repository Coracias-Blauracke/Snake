from board.board_object import BoardObject
from board.fruit.fruit_type import FruitType


class Fruit(BoardObject):

    def __init__(self, x = 0, y = 0, type = FruitType.APPLE):
        super().__init__(x, y)
        self.type = type