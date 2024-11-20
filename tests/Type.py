

from time import time
from CodingTools2.Type import *


_list = [
    1, 1
]


def test(_vector):
    s = time()
    for i in range(100000):
        _vector = _vector + _vector
        ...
    print(time() - s)
    return


if __name__ == '__main__':
    test(Vector1D(_list))
    test(Vector(_list))
    ...
