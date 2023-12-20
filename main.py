from control.game_controller_factory import GameControllerFactory


if __name__ == '__main__':
    game_controller_factory = GameControllerFactory()
    game_controller = game_controller_factory.create_game_controller()

    game_controller.run()