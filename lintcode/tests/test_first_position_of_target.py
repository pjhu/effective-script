import unittest
from lintcode.first_position_of_target import FirstPositionOfTarget


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = FirstPositionOfTarget()

    def tearDown(self):
        del self.obj

    # first
    def test_first_position_of_target(self):
        self.assertEqual(self.obj.binary_search([1, 4, 4, 5, 7, 7, 8, 9, 9, 10], 1), 0)

    # middle
    def test_first_position_of_target_2(self):
        self.assertEqual(self.obj.binary_search([2, 6, 8, 13, 15, 17, 17, 18, 19, 20], 15), 4)

    # last
    def test_first_position_of_target_3(self):
        self.assertEqual(self.obj.binary_search([2, 2, 3, 4, 5, 6, 8, 13, 17, 18], 17), 8)

    # duplicate
    def test_first_position_of_target_3(self):
        self.assertEqual(self.obj.binary_search([3, 4, 5, 8, 8, 8, 8, 10, 13, 14], 8), 3)


if __name__ == '__main__':
    unittest.main()
