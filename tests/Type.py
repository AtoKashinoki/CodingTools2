

from CodingTools2.Type import *


_list = [
    [
        [
            0
            for _ in range(10)
        ]
        for _ in range(10)
    ]
    for _ in range(2)
]


if __name__ == '__main__':

    vector = Vector(_list)
    print(vector.size)
    ...
