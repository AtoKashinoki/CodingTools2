

from time import time
from CodingTools2.Type import *


_list = [
    1, 0
]


if __name__ == '__main__':
    vector = Vector(_list)
    vector2 = Vector(_list)

    print(-vector < vector2)
    print(vector.eq_data(vector2))
    print(10 in vector)
    print(vector, vector2)
    ...
