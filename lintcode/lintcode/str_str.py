# -*- utf-8 -*-
"""
thirteenth
http://www.lintcode.com/en/problem/strstr/
"""
import profile


class StrStr(object):
    def str_str(self, source, target):
        # write your code here
        if '' == target:
            return 0
        if not source or not target:
            return -1
        return source.find(target)

    def str_str_2(self, source, target):
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while j < len_t:
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1

if __name__ == '__main__':
    obj = StrStr()
    print(profile.run('obj.str_str("abcdabcdefg", "bcd")'))
