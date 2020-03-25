# -*- utf-8 -*-
"""
eighth
http://www.lintcode.com/en/problem/rotate-string/
"""

class RotateString(object):
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotate_string(self, s, offset):
        # write you code here
        if not s:
            return s
        for i in range(offset % len(s)):
            temp = s.pop()
            s.insert(0, temp)
        return s

if __name__ == '__main__':
    obj = RotateString()
    print(obj.rotate_string(list("abcdefg"), 3))
