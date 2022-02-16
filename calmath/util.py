import math
from calmath.circle import Circle
from calmath.vec2 import vec2
from calmath.line import Line
from calmath.latex import evalLatex

# Simple stuff
def clamp(i: float, _min: float, _max: float):
    return max(min(i,_max),_min)
def remap(min1: float,max1: float,min2: float,max2: float,val: float):
    val-=min1
    val/=(max1-min1)
    val*=(max2-min2)
    val+=min2
    return val

# Distances
def distPointPoint(vec1: vec2, vec2_: vec2=vec2(0,0)):
    return math.sqrt( (vec1.x-vec2_.x)**2 + (vec1.y-vec2_.y)**2 )
def distPointCircle(p: vec2,c:Circle):
    return max(distPointPoint(p,c.pos)-c.radius,0)
def distPointRing(p: vec2,c:Circle):
    return abs(distPointPoint(p,c.pos)-c.radius)
def distCircleCircle(c1:Circle,c2:Circle):
    return distPointPoint(c1.pos,c2.pos)-c1.radius-c2.radius
def dist(a: vec2 or Circle,b: vec2 or Circle):
    if isinstance(a,vec2):
        if isinstance(b,vec2):
            return distPointPoint(a,b)
        elif isinstance(b,Circle):
            return distPointCircle(a,b)
    elif isinstance(a,Circle):
        if isinstance(b,vec2):
            return distPointCircle(b,a)
        elif isinstance(b,Circle):
            return distCircleCircle(a,b)
    


# Intersections
def lineLineIntersect(l1: Line, l2: Line):
    if l1.m == l2.m:
        return None
    x=(l2.b-l1.b)/(l1.m-l2.m)
    y=l1.getY(x)
    return vec2(x,y)
def lineCircleIntersect(l: Line, c: Circle):
    try:
        x1=evalLatex(
            r"\frac{-a+mb-md+\sqrt{-m^2a^2+2mad-2mab+m^2g^2+g^2+2d*b-d^2-b^2}}{-1-m^2}",
            {
                'a': c.pos.x,
                'd': c.pos.y,
                'g': c.radius,
                'b': l.b,
                'm': l.m
            }
        )
        y1=l.getY(x1)
    except ValueError:
        x1=None
        y1=None
    try:
        x2=evalLatex(
            r"-\frac{md+a+\sqrt{-m^2a^2+2mad-2mab+m^2g^2+g^2+2d*b-d^2-b^2}-mb}{-m^2-1}",
            {
                'a': c.pos.x,
                'd': c.pos.y,
                'g': c.radius,
                'b': l.b,
                'm': l.m
            }
        )
        y2=l.getY(x2)
    except ValueError:
        x2=None
        y2=None
    
    if x1!=None:
        if x2==None:
            return vec2(x1,y1)
        else:
            return (vec2(x1,y1),vec2(x2,y2))
    else:
        if x2==None:
            return None
        else:
            return vec2(x2,y2)
