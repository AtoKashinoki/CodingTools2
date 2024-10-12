from CodingTools2.Inheritance import DataClass


class Test(DataClass):
    test: str = "test1"
    test3: str = "test3"
    ...


if __name__ == "__main__":
    test = Test(test="test2")
    test.test2 = 1
    print(test.test, Test.test)
    print(test)

    print(test.keys())
    ...
