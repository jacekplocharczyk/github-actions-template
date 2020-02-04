import numpy as np

from project import utils


def test_add_arrays():
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    expected_result = np.array([2, 4, 6])
    result = utils.add_arrays(a, b)
    np.testing.assert_array_equal(result, expected_result)
