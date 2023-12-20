import pygame
from board.snake.snake_direction import SnakeDirection

from input_controller.game_input import GameInput


class GameController:

    def __init__(self, board, input_controller):
        self.board = board
        self.renderers = []
        self.input_controller = input_controller
        

    def add_renderer(self, renderer):
        self.renderers.append(renderer)

    def run(self):
        while True:
            self.handle_inputs()
            self.board.update()
            self.render()


    def handle_inputs(self):
        inputs = self.input_controller.get_inputs()
        for input in inputs:
            if input == GameInput.UP:
                self.board.snake.change_direction(SnakeDirection.UP)
                break
            elif input == GameInput.DOWN:
                self.board.snake.change_direction(SnakeDirection.DOWN)
                break
            elif input == GameInput.LEFT:
                self.board.snake.change_direction(SnakeDirection.LEFT)
                break
            elif input == GameInput.RIGHT:
                self.board.snake.change_direction(SnakeDirection.RIGHT)
                break
            elif input == GameInput.QUIT:
                pygame.quit()
                quit()

    def render(self):
        for renderer in self.renderers:
            renderer.render(self.board)
            pygame.time.wait(100)