class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        print(f'Координаты: x {self.x}, y {self.y}')

    def __repr__(self):
        return f'<Point x: {self.x}, y: {self.y}>'

my_point = Point(2, 3)

print(my_point)