import pygame
from pygame.colordict import THECOLORS
from board.fruit.fruit_type import FruitType
from renderer.base_renderer import BaseRenderer


class PygameRenderer(BaseRenderer):
    def __init__(self, width, heigth, tile_size):
        super().__init__()
        self.tile_size = tile_size
        pygame.init()
        self.display = pygame.display.set_mode((width * tile_size, heigth * tile_size))
        pygame.display.set_caption('Snake')

    def render(self, board):
        self.display.fill(THECOLORS['white'])
        
        for x in range(board.width):
            for y in range(board.height):
                screen_x = x * self.tile_size
                screen_y = y * self.tile_size
                if board.snake.head.x == x and board.snake.head.y == y:
                    pygame.draw.rect(self.display, THECOLORS['palevioletred3'], (screen_x, screen_y, self.tile_size, self.tile_size))
                elif any(body_part.x == x and body_part.y == y for body_part in board.snake.body):
                    pygame.draw.rect(self.display, THECOLORS['palevioletred1'], (screen_x, screen_y, self.tile_size, self.tile_size))
                elif board.fruit.x == x and board.fruit.y == y:
                    if board.fruit.type == FruitType.APPLE:
                        pygame.draw.rect(self.display, THECOLORS['red'], (screen_x, screen_y, self.tile_size, self.tile_size))
                    elif board.fruit.type == FruitType.BANANA:
                        pygame.draw.rect(self.display, THECOLORS['orange'], (screen_x, screen_y, self.tile_size, self.tile_size))
                    elif board.fruit.type == FruitType.ORANGE:
                        pygame.draw.rect(self.display, THECOLORS['yellow'], (screen_x, screen_y, self.tile_size, self.tile_size))
                else:
                    pygame.draw.rect(self.display, THECOLORS['palegreen'], (screen_x, screen_y, self.tile_size, self.tile_size))
        pygame.display.update()