from ..types import Vector


def filter_zeros_from_vector(vector: Vector) -> Vector:
    """Returns only these values in vector which is other than zero (with order saved).

    Args:
        vector - flat numpy vector

    Returns:
        flat numpy vector

    Example:
        sample_vectorvector = np.ndarray([1,2,3,0,5,0,7])

        filter_zeros_from_vector(sample_vector)

        >>> [1,2,3,5,7]
    """
    return vector[vector != 0]
