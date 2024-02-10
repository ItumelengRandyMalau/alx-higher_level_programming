#!/usr/bin/python3
""" Defines a Rectangle clss"""


from base import Base


class Rectangle(Base):
    """ Represents a derived class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width_val):
        if not isinstance(width_val, int):
            raise TypeError("width must be an integer")
        if width_val <= 0:
            raise ValueError("width must be > 0")
        self.__width = width_val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height_val):
        if not isinstance(height_val, int):
            raise TypeError("height must be an integer")
        if height_val <= 0:
            raise ValueError("height must be > 0")
        self.__height = height_val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_val):
        if not isinstance(x_val, int):
            raise TypeError("x must be an integer")
        if x_val < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y_val):
        if not isinstance(y_val, int):
            raise TypeError("y must be an integer")
        if y_val < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_val

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
