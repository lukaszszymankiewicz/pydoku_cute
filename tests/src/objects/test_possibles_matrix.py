import numpy as np

from src.objects import PossiblesMatrix


def test_find_sole_candidates_return_proper_number_of_values():
    # GIVEN
    possibles_matrix = PossiblesMatrix()

    # WHEN
    possibles_matrix.array[:, :, :] = 0
    possibles_matrix.array[0, 0, 1] = 1
    possibles_matrix.array[0, 1, 1] = 1
    possibles_matrix.array[2, 2, 2] = 2
    possibles_matrix.array[3, 2, 4] = 4

    possibles_matrix.find_sole_candidate(axis=1)
