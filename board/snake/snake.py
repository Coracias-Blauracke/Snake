from board.snake.body_part_factory import BodyPartFactory
from board.snake.body_part_type import BodyPartType
from board.snake.snake_direction import SnakeDirection


class Snake:
    
    def __init__(self, x, y, body_part_factory):
        self.body_part_factory = body_part_factory
        self.head = self.body_part_factory.create_body_part(x, y, BodyPartType.HEAD)
        self.body = []
        self.direction = SnakeDirection.RIGHT

    def change_direction(self, direction):
        if self.direction != SnakeDirection.UP and direction == SnakeDirection.DOWN:
            self.direction = SnakeDirection.DOWN
        elif self.direction != SnakeDirection.DOWN and direction == SnakeDirection.UP:
            self.direction = SnakeDirection.UP
        elif self.direction != SnakeDirection.LEFT and direction == SnakeDirection.RIGHT:
            self.direction = SnakeDirection.RIGHT
        elif self.direction != SnakeDirection.RIGHT and direction == SnakeDirection.LEFT:
            self.direction = SnakeDirection.LEFT
    
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x = self.head.x
        self.body[0].y = self.head.y

        if self.direction == SnakeDirection.UP:
            self.head.y -= 1
        elif self.direction == SnakeDirection.DOWN:
            self.head.y += 1
        elif self.direction == SnakeDirection.LEFT:
            self.head.x -= 1
        elif self.direction == SnakeDirection.RIGHT:
            self.head.x += 1

    def grow(self):
        x = self.head.x
        y = self.head.y
        type = BodyPartType.HEAD
        
        if len(self.body) != 0:
            x = self.body[len(self.body) - 1].x
            y = self.body[len(self.body) - 1].y
            type = BodyPartType.BODY
        
        new_body_part = self.body_part_factory.create_body_part(x, y, type)
        self.body.append(new_body_part)


