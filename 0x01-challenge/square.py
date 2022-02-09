#!/usr/bin/python3
""" A module for handling squares. """


class square:
    """ Represents a rectangle with equal sides. """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a new square. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Computes the area of this square. """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Computes the perimeter of this square. """
        return (self.width * 4)

    def __str__(self):
        """ Computes the string format of this square. """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
