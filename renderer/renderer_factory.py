from renderer.console_renderer import ConsoleRenderer
from renderer.pygame_renderer import PygameRenderer
from renderer.renderer_type import RendererType


class RendererFactory:

    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size

    def create_renderer(self, renderer_type):
        if renderer_type == RendererType.CONSOLE:
            return ConsoleRenderer()
        elif renderer_type == RendererType.PYGAME:
            return PygameRenderer(self.width, self.height, self.tile_size)
        else:
            raise Exception("Renderer not supported: " + renderer_type)