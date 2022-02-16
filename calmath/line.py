from calmath.vec2 import vec2

class Line:
    def __init__(self,m:float,b:float):
        """Make a straight line using the slope intercept equation (y=mx+b)
        
        Keyword arguments:
        m -- the slope of the line
        b -- the Y intercept
        """
        self.m=m
        self.b=b
    def __str__(self) -> str:
        return f"(m={self.m},b={self.b})"
    def getY(self, x: float):
        """Get the Y position at a certain X value."""
        return self.m*x+self.b
    def getX(self, y: float):
        """Get the X position at a certain Y value."""
        return (y-self.b)/self.m
    def fromPoints(p1: vec2, p2: vec2):
        m=(p1.y-p2.y)/(p1.x-p2.x)
        return Line(m,-m*p1.x+p1.y)
class Segment:
    def __init__(self):
        pass