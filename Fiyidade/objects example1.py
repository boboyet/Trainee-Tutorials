class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material
    def ride(self):
        print("my bicyle is moving")
    def brake(self):
        print("bicyle stopping")
bike1 = Bike("yellow", "metal")
print(bike1.colour)
print(bike1.frame_material)
bike1.ride()
bike1.brake()
