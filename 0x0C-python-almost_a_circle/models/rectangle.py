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
        """Gets the value of width"""
        return self.__width

    @width.setter
    def width(self, width_val):
        """sets the value of width"""
        if not isinstance(width_val, int):
            raise TypeError("width must be an integer")
        if width_val <= 0:
            raise ValueError("width must be > 0")
        self.__width = width_val

    @property
    def height(self):
        """Gets the value of height"""
        return self.__height

    @height.setter
    def height(self, height_val):
        """sets the value of height"""
        if not isinstance(height_val, int):
            raise TypeError("height must be an integer")
        if height_val <= 0:
            raise ValueError("height must be > 0")
        self.__height = height_val

    @property
    def x(self):
        """Gets the x value"""
        return self.__x

    @x.setter
    def x(self, x_val):
        """Sets value to x"""
        if not isinstance(x_val, int):
            raise TypeError("x must be an integer")
        if x_val < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_val

    @property
    def y(self):
        """Gets the value of y"""
        return self.__y

    @y.setter
    def y(self, y_val):
        """Sets value to y"""
        if not isinstance(y_val, int):
            raise TypeError("y must be an integer")
        if y_val < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_val

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with the character #"""
        for i in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """str method, returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes."""
        if args:
            for i in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x == arg
                elif i == 4:
                    self.height = arg
                else:
                    continue
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """Dictionary representation of rectangle class"""
        rect_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

        return rect_dict
