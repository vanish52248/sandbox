import pytest
from calc import calc

params = [
    (1, 2, 3, 6),
    (3, 4, 7, 14),
    (4, 5, 6, 15),
]


@pytest.mark.parametrize(
    "param_a, param_b, param_c, result",
    params)
def test_calc(param_a, param_b, param_c, result):
    ans = calc(param_a, param_b, param_c)
    assert ans == result
