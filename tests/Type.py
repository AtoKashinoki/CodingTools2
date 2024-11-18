

from time import time
from CodingTools2.Type import *


_list = [
    0, 0
]


if __name__ == '__main__':
    _list[0] = 1
    vector = Vector(_list)
    s = time()
    for _ in range(1000000):
        vector = 1.1 * vector
        ...
    print(time() - s)

    print(vector)
    ...
