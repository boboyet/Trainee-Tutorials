class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __call__(self):
        print("Hey, I was called!!!")


v1 = Vector(10, 30)
v2 = Vector(90, 20)
v3 = v1 + v2

v3()
print(v3)
