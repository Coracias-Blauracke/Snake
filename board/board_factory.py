from board.board import Board
from board.fruit.fruit_factory import FruitFactory
from board.snake.snake_factory import SnakeFactory


class BoardFactory:

    def create_board(self, width, height):
        snake_length = 2
        snake_factory = SnakeFactory()
        snake = snake_factory.create_snake(width / 2, height / 2, snake_length)
        fruit_factory = FruitFactory()
        return Board(width, height, snake, fruit_factory)