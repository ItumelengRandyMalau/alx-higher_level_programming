#!/usr/bin/python3
"""Defines a class: Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.

        If attrs is a list of strings, only represent the attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
