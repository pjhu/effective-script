# -*- utf-8 -*-
"""
third
http://www.lintcode.com/en/problem/digit-counts/

Count the number of k's between 0 and n. k can be 0 - 9.
"""
import profile


class DigitCounts(object):

    def digit_counts(self, k, n):
        a = ''.join(map(lambda x: str(x), range(n+1)))
        return a.count(str(k))

if __name__ == '__main__':
    obj = DigitCounts()
    print(profile.run("obj.digit_counts(1, 5)"))
