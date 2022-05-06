import mathlib
import pytest

@pytest.mark.parameterize_testing("test_output, expected_output",
                         [
                             (3, 9),
                             (2, 4),
                             (9, 81)
                         ])

def test_cal_square(test_output, expected_output):
    result = mathlib.cal_square(test_output)
    assert result == expected_output