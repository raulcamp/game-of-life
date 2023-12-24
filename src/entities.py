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
# TODO: Implement a Point object


@dataclass
class Cell:
    """Represents a cell"""
    x: int
    y: int
    size: int
    color: tuple

    def get_pos(self):
        """Returns the coordinate of the cell"""
        return self.x, self.y


if __name__ == "__main__":
    pass
