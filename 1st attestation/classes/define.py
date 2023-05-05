class Shape: 
    def area(self):
        print(0)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        print(self.length ** 2)
       
shape1 = Shape()
sq = Square(2)
shape1.area()
sq.area()