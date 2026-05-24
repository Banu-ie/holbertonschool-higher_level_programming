#!/usr/bin/python3
"""Module that returns the dictionary description of an object"""


def class_to_json(obj):
    """Returns the dictionary representation of a class instance"""
    return obj.__dict__
