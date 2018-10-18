from Circle import Circle


def main():
    # Create a circle with radius 1
    circle1 = Circle()
    print("the area of the circle of radius",
          circle1.radius, "is", circle1.getArea())
    circle2 = Circle(25)
    print("the area of the circle of radius",
          circle2.radius, "is", circle2.getArea())
    circle3 = Circle(125)
    print("the area of the circle of radius",
          circle3.radius, "is", circle3.getArea())

    # modify circle radius
    circle2.radius = 100
    print("the area of circle of radius", circle2.radius, "is", circle2.getArea())


main()
