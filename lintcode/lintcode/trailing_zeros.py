# -*- coding utf-8 -*-
"""
second
http://www.lintcode.com/en/problem/trailing-zeros/

Write an algorithm which computes the
number of trailing zeros in n factorial.
"""


class TrailingZero(object):
    """
    :param n: a integer
    :return: ans a integer
    """
    def trailing_zeros(self, n):
        counter = 0
        tmp = n
        while tmp:
            tmp //= 5
            counter += tmp
        return counter


if __name__ == "__main__":
    obj = TrailingZero()
    print(obj.trailing_zeros(100))
