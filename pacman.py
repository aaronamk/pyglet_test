#Import statements
import pyglet
from pyglet.window import Window, key

from entity import Entity
import util
from util import Direction

class Pacman(Entity):
    """Pacman Entity controlled by user.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, pyglet.resource.image('player.jpg'), **kwargs)

        self.image.width = 48
        self.image.height = 48
        util.center_image(self.image)
        
        self.speed = 100
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.desired_direction = Direction.West

    def update(self, dt):
        """This method should be called every frame.
        """
        super(Pacman, self).update(dt)

        if self.key_handler[key.W]:
            self.desired_direction = Direction.North
            self.turn(Direction.North)
        if self.key_handler[key.S]:
            self.desired_direction = Direction.South
            self.turn(Direction.South)
        if self.key_handler[key.D]:
            self.desired_direction = Direction.East
            self.turn(Direction.East)
        if self.key_handler[key.A]:
            self.desired_direction = Direction.West
            self.turn(Direction.West)
        
        if self.desired_direction and self.check_turn():
            self.turn(self.desired_direction)
            self.desired_direction = None

        self.check_bounds()

    def check_turn(self):
        if not (self.x + 25) % 50:
            return True

    def turn(self, d):
        """Sets the direction of the lady
            d -- Direction
        """
        self.speed_x = d.value[0] * self.speed
        self.speed_y = d.value[1] * self.speed
        self.rotation = d.value[2]
        self.scale_x = -1 if d is Direction.West else 1

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0