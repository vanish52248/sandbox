import pytest
from unittest.mock import patch
from calc import calc

@patch("calc.result_flg", False)
def test_calc(mocker):
   
    result = calc()

    assert result == {"result_flg": False}
    