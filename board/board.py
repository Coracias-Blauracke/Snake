import random
from board.fruit.fruit_type import FruitType


class Board:

    def __init__(self, width, height, snake, fruit_factory):
        self.width = width
        self.height = height
        self.snake = snake
        self.fruit_factory = fruit_factory
        self.put_fruit()

    def update(self):
        self.snake.move()
        self.teleport_snake_to_opposite_side()
        if self.is_collision_with_fruit():
            self.snake.grow()
            self.put_fruit()

    def put_fruit(self):
        new_fruit_x = random.randint(0, self.width - 1)
        new_fruit_y = random.randint(0, self.height - 1)
        while self.is_collision_with_snake(new_fruit_x, new_fruit_y):
            new_fruit_x = random.randint(0, self.width - 1)
            new_fruit_y = random.randint(0, self.height - 1)
        
        self.fruit = self.fruit_factory.create_fruit(new_fruit_x, new_fruit_y, self.random_fruit_type())

    def is_collision_with_fruit(self):
        return self.snake.head.x == self.fruit.x and self.snake.head.y == self.fruit.y
    
    def teleport_snake_to_opposite_side(self):
        if self.snake.head.x < 0:
            self.snake.head.x = self.width - 1
        elif self.snake.head.x >= self.width:
            self.snake.head.x = 0
        elif self.snake.head.y < 0:
            self.snake.head.y = self.height - 1
        elif self.snake.head.y >= self.height:
            self.snake.head.y = 0

    def is_collision_with_snake(self, x, y):
        if self.snake.head.x == x and self.snake.head.y == y:
            return True
        for body_part in self.snake.body:
            if body_part.x == x and body_part.y == y:
                return True
        return False
    
    def random_fruit_type(self):
        return random.choice(list(FruitType))