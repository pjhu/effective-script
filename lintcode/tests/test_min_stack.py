import unittest
from lintcode.min_tack import MinStack


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = MinStack()

    def tearDown(self):
        del self.obj

    def test_min_stack(self):
        self.obj.push(1), self.obj.pop(), self.obj.push(2), \
            self.obj.push(3), self.obj.min(), self.obj.push(1),
        self.assertEqual(self.obj.min(), 1)


if __name__ == '__main__':
    unittest.main()
