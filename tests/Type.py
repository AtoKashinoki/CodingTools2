

from CodingTools2.Type import *
from CodingTools2.Decorator import Test


_list = [
    1, 1
]


@Test.Time
@Test.Repeat(10)
@Test.BlankLine
@Test.Time
@Test.Repeat(100000)
def test(_vector):
    _vector = _vector * _vector
    return


if __name__ == '__main__':
    vector = Vector1D(_list)
    vector = Vector1D(vector)
    test(vector)
    vector =Vector(_list)
    test(vector)
    ...
