from copy import deepcopy
from time import time
from CodingTools2.Inheritance import DataClass


class Test(DataClass):
    test: str = "test1"
    test3: str = "test3"
    __test4: str ="test4"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__test5 = "test5"
        return
    ...


if __name__ == "__main__":
    test = Test(test="test2")
    test.test2 = 1
    s = time()
    for _ in range(1000000):
        test += {"a": 0}
        ...
    print(time() - s)
    test["key"] = "key"
    test += {"test6": "test6"}
    test2 = deepcopy(test)
    del test2["test2"]

    print(test, test2, sep="\n")
    print(test > test2)

    print("test" in test)
    ...
