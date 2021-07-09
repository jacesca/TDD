import pytest

from features.as_numpy import get_data_as_numpy_array
import numpy as np
import os

@pytest.fixture
def clean_data_file():
    file_path = "clean.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n7892\t298140\n501\t738293\n")
    yield file_path
    os.remove(file_path)

class TestGetDataAsNumpyArray(object):
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                            ])
        actual = get_data_as_numpy_array(clean_data_file, num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert (actual == expected).all()
    