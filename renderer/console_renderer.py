import os
from board.fruit.fruit_type import FruitType
from renderer.base_renderer import BaseRenderer


class ConsoleRenderer(BaseRenderer):

    def __init__(self):
        super().__init__()

    def render(self, board):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        for y in range(board.width):
            for x in range(board.height):
                if board.snake.head.x == x and board.snake.head.y == y:
                    print("P", end="")
                elif any(body_part.x == x and body_part.y == y for body_part in board.snake.body):
                    print("=", end="")
                elif board.fruit.x == x and board.fruit.y == y:
                    if board.fruit.type == FruitType.APPLE:
                        print("A", end="")
                    elif board.fruit.type == FruitType.BANANA:
                        print("B", end="")
                    elif board.fruit.type == FruitType.ORANGE:
                        print("O", end="")
                else:
                    print(".", end="")
            print()