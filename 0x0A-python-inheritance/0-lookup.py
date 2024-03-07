#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list an object's available attributes"""
    return (dir(obj))