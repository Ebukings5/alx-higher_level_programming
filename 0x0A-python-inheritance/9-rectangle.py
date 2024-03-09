#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):

        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        super().integer_validator("width", width)
        self.width = width
        super().integer_validator("height", height)
        self.height = height
    
    def area(self):
        """Return the are of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a rectangle."""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
