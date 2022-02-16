import math
from calmath.vec2 import vec2

PolPoint=None

degToRad=math.radians
radToDeg=math.degrees

degToSlope=lambda d: math.tan(degToRad(d))
radToSlope=math.tan

slopeToRad=math.atan
slopeToDeg=lambda s: radToDeg(math.atan(s))

def polarToCart(p: PolPoint) -> vec2:
    """Convert a polar point (r, theta) to a cartesian point (x,y)"""
    return vec2(
        math.cos(p.theta)*p.r,
        math.sin(p.theta)*p.r
    )
def cartToPolar(p: vec2) -> PolPoint:
    return PolPoint(
        math.sqrt(p.x**2 + p.y**2),
        math.atan(p.y/p.x)
    )

class PolPoint:
    def __init__(self,r: float, theta: float):
        """Define a polar point.\n
        r : the radius (distance from (0,0))\n
        theta : theta is the radians (0 is right, pi is left)"""
        self.r=r
        self.theta=theta
    def __str__(self) -> str:
        return f"({self.r},{self.theta})"