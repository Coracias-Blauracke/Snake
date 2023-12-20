from board.board_factory import BoardFactory
from control.game_controller import GameController
from input_controller.input_controller_factory import InputControllerFactory
from input_controller.input_controller_type import InputControllerType
from renderer import pygame_renderer
from renderer.renderer_factory import RendererFactory
from renderer.renderer_type import RendererType


class GameControllerFactory:

    def create_game_controller(self):
        width = 20
        height = 20
        tile_size = 20
        board_factory = BoardFactory()
        board = board_factory.create_board(width, height)
        input_controller_factory = InputControllerFactory()
        pygame_input_controller = input_controller_factory.create_input_controller(InputControllerType.PYGAME)

        renderer_factory = RendererFactory(width, height, tile_size)
        console_renderer = renderer_factory.create_renderer(RendererType.CONSOLE)
        pygame_renderer = renderer_factory.create_renderer(RendererType.PYGAME)
        game_controller = GameController(board, pygame_input_controller)
        game_controller.add_renderer(console_renderer)
        game_controller.add_renderer(pygame_renderer)

        return game_controller