from board.snake.body_part import BodyPart
from board.snake.body_part_type import BodyPartType


class BodyPartFactory:

    def create_body_part(self, x = 0, y = 0, type = BodyPartType.BODY):
        return BodyPart(x, y, type)