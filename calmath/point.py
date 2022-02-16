from calmath.vec2 import vec2
from calmath.polar import *

class Point:
    def __init__(self, a):
        self.x=None
        self.y=None
        if isinstance(a,vec2):
            self.x=a.x
            self.y=a.y
        elif isinstance(a,PolPoint):
            pos=polarToCart(a)
            self.x=pos.x
            self.y=pos.y
        pol=cartToPolar(vec2(self.x,self.y))
        self.r=pol.r
        self.theta=pol.theta
    def set_r(self,r:float):
        self.r=r
        pos=polarToCart(self.r,self.theta)
        self.x=pos.x
        self.y=pos.y
    def get_r(self):
        return cartToPolar(vec2(self.x,self.y)).r
    r=property(get_r,set_r)
        