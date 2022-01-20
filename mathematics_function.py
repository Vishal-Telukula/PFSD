import math
import pytest


@pytest.mark.parameter('x,y,z',
                       [
                           (4, 3, 10),('hello', 'world', 'hello world'),(25.5, 10.5, 63)
                       ]
                       )
def test_add(x, y, z):
    assert math.func.add(x, y) == z
