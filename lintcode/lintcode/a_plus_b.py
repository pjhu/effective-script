# -*- coding: utf-8 -*-
"""
first
http://www.lintcode.com/en/problem/a-b-problem/

Write a function that add two numbers A and B.
You should not use + or any arithmetic operators
"""


class IntegerPlus(object):
    """
    :param integer_a: The first integer
    :param integer_b: The second integer
    :return: The sum of a and b
    """
    def aplusb(self, integer_a, integer_b):
        """write your code here, try to do it without arithmetic operators."""
        while integer_b:
            integer_c = integer_a & integer_b
            integer_a = (integer_a ^ integer_b) & 0xffffffff
            integer_b = (integer_c << 1) & 0xffffffff
        return integer_a

    def aplusb2(self, a, b):
        import ctypes
        a = ctypes.c_int32(a).value
        b = ctypes.c_int32(b).value
        while b != 0:
            carry = ctypes.c_int32(a & b).value
            a = ctypes.c_int32(a ^ b).value
            b = ctypes.c_int32(carry << 1).value
        return a

if __name__ == "__main__":
    obj = IntegerPlus()
    print(obj.aplusb2(100, -99))
