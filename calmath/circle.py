from calmath.vec2 import vec2
from loguru import logger
import math

class Circle:
    def __init__(self, pos: vec2, radius: float):
        self.pos=pos
        self.radius=radius
    @logger.catch
    def getY(self, x: float):
        try:
            a=self.pos.x
            b=self.pos.y
            c=self.radius
            i=math.sqrt(
                (c**2) - ((x-a)**2)
            )
            if i==0:
                return i+self.pos.y
            return [i+b,-i+b]
        except ValueError:
            return None
    def getX(self, y: float):
        try:
            a=self.pos.x
            b=self.pos.y
            c=self.radius
            i=math.sqrt(
                (c**2) - ((y-b)**2)
            )
            if i==0:
                return i+self.pos.y
            return [i+a,-i+a]
        except ValueError:
            return None