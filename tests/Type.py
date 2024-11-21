

from time import time
from CodingTools2.Type import *


_list = [
    1, 1
]


def test(_vector):
    print(_vector)
    s = time()
    for i in range(100000):
        _vector = _vector * _vector
        ...
    print(time() - s)
    print(_vector)
    return


if __name__ == '__main__':
    vector = Vector1D(_list)
    vector = Vector1D(vector)
    test(vector)
    vector =Vector(_list)
    test(vector)
    ...
