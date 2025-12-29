#!/usr/bin/python3
"""
This module defines a Student class with filtered JSON serialization.
"""


class Student:
    """
    Defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        are included in the result.

        Args:
            attrs: Optional list of attribute names to retrieve.

        Returns:
            A dictionary containing the requested attributes.
        """
        # If attrs is a list, filter the attributes
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

        # Otherwise, return all attributes
        return self.__dict__
