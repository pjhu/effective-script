# -*- utf-8 -*-
import cProfile
from functools import reduce


class Subsets(object):
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        S.sort()
        p = [[S[x] for x in range(len(S)) if i >> x & 1] for i in range(2**len(S))]
        func = lambda x, y: x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))

if __name__ == '__main__':
    obj = Subsets()
    print(cProfile.run('obj.subsets([0])'))
