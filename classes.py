#template for a type of object

class Point():
    #  A method defining how to create a point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)
