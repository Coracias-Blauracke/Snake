from board.fruit.fruit import Fruit


class FruitFactory:

    def create_fruit(self, x, y, fruit_type):
        return Fruit(x, y, fruit_type)