# -*- utf-8 -*-
"""
fourth
http://www.lintcode.com/en/problem/ugly-number-ii/

Ugly number is a number that only have factors 2, 3 and 5.
Design an algorithm to find the nth ugly number.
The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
"""
import profile


class NthUglyNumber(object):

    def _find_next_ugly_number(self, current_ugly_list):
        min2 = [x * 2 for x in current_ugly_list if x*2 > current_ugly_list[-1]][0]
        min3 = [x * 3 for x in current_ugly_list if x*3 > current_ugly_list[-1]][0]
        min5 = [x * 5 for x in current_ugly_list if x*5 > current_ugly_list[-1]][0]
        return min(min2, min3, min5)

    def nth_ugly_number(self, n):
        ugly_list = [1]
        for i in range(n-1):
            ugly_list.append(self._find_next_ugly_number(ugly_list))
        return ugly_list[-1]

if __name__ == "__main__":
    obj = NthUglyNumber()
    print(profile.run("obj.nth_ugly_number(9)"))
