import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5",8), ("4*9",36), ("3-9",8)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval_2(test_input, expected):
    assert eval(test_input) == expected