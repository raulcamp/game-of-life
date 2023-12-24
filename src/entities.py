"""Game of Life entities, objects, and classes"""
from dataclasses import dataclass


@dataclass
class Object:
    """Represents an object"""
    x: int
    y: int
    width: int
    height: int
    color: tuple


@dataclass
class Cell:
    """Represents a cell"""
    x: int
    y: int
    size: int
    color: tuple


if __name__ == "__main__":
    pass
