from input_controller.input_controller_type import InputControllerType
from input_controller.pygame_input_controller import PygameInputController


class InputControllerFactory:

    def create_input_controller(self, input_controller_type):
        if input_controller_type == InputControllerType.PYGAME:
            return PygameInputController()
        else:
            raise Exception("Input controller not supported: " + input_controller_type)