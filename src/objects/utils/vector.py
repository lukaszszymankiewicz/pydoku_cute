from src.static.types import Vector


def filter_zeros_from_vector(vector: Vector) -> Vector:
    return vector[vector != 0]
