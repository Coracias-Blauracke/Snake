import pygame

from input_controller.game_input import GameInput
from input_controller.input_controller import InputController


class PygameInputController(InputController):

    def __init__(self):
        super().__init__()
        self.pygame_key_map = {
            pygame.K_w: GameInput.UP,
            pygame.K_UP: GameInput.UP,
            pygame.K_s: GameInput.DOWN,
            pygame.K_DOWN: GameInput.DOWN,
            pygame.K_a: GameInput.LEFT,
            pygame.K_LEFT: GameInput.LEFT,
            pygame.K_d: GameInput.RIGHT,
            pygame.K_RIGHT: GameInput.RIGHT,
            pygame.K_q: GameInput.QUIT
        }

    def get_inputs(self):
        inputs = []
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in self.pygame_key_map:
                inputs.append(self.pygame_key_map[event.key])

        return inputs
