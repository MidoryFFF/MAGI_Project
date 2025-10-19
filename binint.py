class BinInt:
    x: bool = False
    y: bool = False

    def __add__(self, num: int) -> int:
        if self.x:
            return num + int(self.y * (-1))
        else:
            return num + self.y

    def set(self, x: int, y: int):
        self.x = bool(x > 0)
        self.y = bool(y > 0)

    def get(self):
        if self.x:
            return self.y * (-1)
        else:
            return self.y
    
    def getTrueValues(self):
        return [self.x, self.y]