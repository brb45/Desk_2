import pytest
class MissingCoordException(Exception):
    """Exception raised when X or Y is not present in the data."""


class MissingBothCoordException(Exception):
    """Exception raised when both X and Y are not present in the data."""


def sum_x_y(data: dict) -> str:
    if "x" not in data and "y" not in data and "extra" not in data:
        raise MissingBothCoordException("Both X and Y coord missing.")
    if "x" not in data:
        raise MissingCoordException("The Y coordinate is not present in the data.")
    if "y" not in data:
        raise MissingCoordException("The Y coordinate is not present in the data.")
    return data["x"] + data["y"]

def test_sum_x_y_has_x_missing_coord():
    data = {"extra": 1, "y": 2}
    with pytest.raises(MissingCoordException) as exc:
        sum_x_y(data)
    # assert "The X coordinate is not present in the data." in str(exc.value)
