import unittest


def parse():
    items = []

    for item in range(10):
        items.append(item)

    return items


def parse2():
    for item in range(10):
        yield item


def fibo(x):
    if x == 0:
        resp = 0
    elif x == 1:
        resp = 1
    else:
        return fibo(x - 1) + fibo(x - 2)
    return resp


class TestClass(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    assert fibo(5) == 5
