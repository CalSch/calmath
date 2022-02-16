vec2=None
class vec2:
    def __init__(self,x: float, y: float) -> None:
        self.x=float(x)
        self.y=float(y)
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    def addVec(self,vec: vec2):
        return vec2(
            self.x+vec.x,
            self.y+vec.y,
        )
    def subVec(self,vec: vec2):
        return vec2(
            self.x-vec.x,
            self.y-vec.y,
        )
    def multVec(self,vec: vec2):
        return vec2(
            self.x*vec.x,
            self.y*vec.y,
        )
    def divVec(self,vec: vec2):
        return vec2(
            self.x/vec.x,
            self.y/vec.y,
        )
    
    def addNum(self,num: float):
        return vec2(
            self.x+num,
            self.y+num
        )
    def subNum(self,num: float):
        return vec2(
            self.x-num,
            self.y-num
        )
    def multNum(self,num: float):
        return vec2(
            self.x*num,
            self.y*num
        )
    def divNum(self,num: float):
        return vec2(
            self.x/num,
            self.y/num
        )
    
    def add(self,i: vec2 or float):
        if isinstance(i,vec2):
            return self.addVec(i)
        elif isinstance(i,float) or isinstance(i,int):
            return self.addNum(i)
    def sub(self,i: vec2 or float):
        if isinstance(i,vec2):
            return self.subVec(i)
        elif isinstance(i,float) or isinstance(i,int):
            return self.subNum(i)
    def mult(self,i: vec2 or float):
        if isinstance(i,vec2):
            return self.multVec(i)
        elif isinstance(i,float) or isinstance(i,int):
            return self.multNum(i)
    def div(self,i: vec2 or float):
        if isinstance(i,vec2):
            return self.divVec(i)
        elif isinstance(i,float) or isinstance(i,int):
            return self.divNum(i)
        
    