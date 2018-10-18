class Rectangle:

    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.height * self.width

    def getPerimeter(self):
        return 2 * (self.width + self.height)
