from RectangleClass import Rectangle


def main():
    rectangle1 = Rectangle(4, 40)
    print('the area of the rectangle of width',
          rectangle1.width, 'and', rectangle1.height,
          'is', rectangle1.getArea(), 'and its perimeter is',
          rectangle1.getPerimeter())

    rectangle2 = Rectangle(3.5, 35.7)
    print('the area of the rectangle of width',
          rectangle2.width, 'and', rectangle2.height,
          'is', rectangle2.getArea(), 'and its perimeter is',
          rectangle2.getPerimeter())


main()
