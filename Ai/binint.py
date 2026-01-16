class BinInt:
    def __init__(self, xV = False, yV =False):
        self.x: bool = bool(xV)
        self.y: bool = bool(yV)

    def __add__(self, num: int) -> int:
        if self.x:
            return num + int(self.y * (-1))
        else:
            return num + self.y

    def set(self, x: int, y: int):
        self.x = bool(x > 0)
        self.y = bool(y > 0)

    def get(self) -> int:
        if self.x:
            return int(self.y * (-1))
        else:
            return int(self.y)

    def getTrueValues(self) -> list[bool]:
        return [self.x, self.y]
    
    def getInt(self):
        return int(self.x << 1) + int(self.y)
