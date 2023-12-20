from board.snake.body_part_factory import BodyPartFactory
from board.snake.snake import Snake


class SnakeFactory:

    def create_snake(self, x, y, length):
        body_part_factory = BodyPartFactory()
        snake = Snake(x, y, body_part_factory)
        for _ in range(length):
            snake.grow()
        return snake