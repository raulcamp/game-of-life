"""Game of Life entities, objects, and classes"""
from dataclasses import dataclass, field


@dataclass
class Object:
    """Represents an object"""
    x: int
    y: int
    width: int
    height: int
    color: tuple
