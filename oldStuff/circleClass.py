from math import pi


class Shape:
    name = ''

    def __str__(self):
        return self.name


class Circle(Shape):
    name = 'Circle'

    def __init__(self, diameter):
        self.diameter = diameter

    def area(self):
        return self._get_radius() ** 2 * pi

    def _get_radius(self):
        return self.diameter / 2

    def perimeter(self):
        return self.diameter * pi

    @staticmethod
    def perimeter(diameter):
        return diameter * pi

    def __str__(self):
        return '{} with radius {}'.format(
            self.name,
            self.radius
        )


class CurvedCircle(Circle):
    name = 'Curved circle'


if __name__ == '__main__':
    # s = CurvedCircle(10)
    # print('circle radius is', s.radius)
    # print('circle perimeter is', s.perimeter())
    # print('circle area is', s.area())
    # print(s)
    # s._get_radius()
    # Circle.area(s)
    # lets compute the perimeter of a cicle
    # WITHOUT A CIRCLE!
    print(Circle.perimeter(10))

