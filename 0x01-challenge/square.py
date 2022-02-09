#!/usr/bin/python3
""" A module for handling squares. """


class Square:
    """Represents a rectangle with equal sides."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a new square. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    # @property
    # def width(self):
    #     """ Gets the width of this square. """
    #     return self.__width

    # @width.setter
    # def width(self, value):
    #     """ Sets the width of this square. """
    #     if type(value) is int or type(value) is float:
    #         if value < 0:
    #             raise ValueError("Value must be >= 0.")
    #         else:
    #             self.__width = value
    #     else:
    #         raise TypeError("Type must be an int or a float.")

    def area_of_my_square(self):
        """ Computes the area of this square. """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ Computes the perimeter of this square. """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Computes the string format of this square. """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
