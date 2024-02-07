#!/usr/bin/python3
"""Defines a class: Student."""


class Student:
    """Represents a student class."""

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

    def to_json(self):
        """Gets a dictionary representation of the Student class."""
        return self.__dict__
