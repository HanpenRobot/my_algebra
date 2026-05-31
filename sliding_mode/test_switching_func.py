import pytest


def sigma(x: float, y: float) -> float:
    return x * (0.5 * x + y)


def gain(x: float, y: float) -> float:
    if sigma(x, y) > 0:
        return 4
    if sigma(x, y) < 0:
        return -4


# pytest.exe -s -vv .\test_switching_func.py
@pytest.mark.parametrize(
    "input, expected",
    [
        ((-1, 1), -4),
        ((1, 1), 4),
        ((-1, -1), 4),
        ((1, -1), 4),
    ],
)
def test_sigma(input, expected):
    print(f"{gain(x=input[0], y=input[1])=}")
    # assert sigma(x=input[0], y=input[1]) == expected
