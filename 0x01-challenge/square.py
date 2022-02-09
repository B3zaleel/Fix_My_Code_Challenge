#!/usr/bin/python3
""" A module for handling squares. """


class square:
    """Represents a rectangle with equal sides."""
    __width = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a new square. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def width(self):
        """ Gets the width of this square. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of this square. """
        if type(value) is int or type(value) is float:
            if value < 0:
                raise ValueError("Value must be >= 0.")
            else:
                self.__width = value
        else:
            raise TypeError("Type must be an int or a float.")

    def area(self):
        """ Computes the area of this square. """
        return self.width * self.width

    def perimeter(self):
        """ Computes the perimeter of this square. """
        return (self.width * 4)

    def __str__(self):
        """ Computes the string format of this square. """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())
