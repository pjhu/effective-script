# -*- utf-8 -*-
import cProfile
import itertools


class Subsets(object):
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # the power set of the empty set has one element, the empty set
        result = [[]]
        for x in S:
            # for every additional element in our set
            # the power set consists of the subsets that don't
            # contain this element (just take the previous power set)
            # plus the subsets that do contain the element (use list
            # comprehension to add [x] onto everything in the
            # previous power set)
            result.extend([subset + [x] for subset in result])
        return result

    def subsets_2(self, S):
        S.sort()
        # 1 << n is 2^n
        # each subset equals to an binary integer between 0 .. 2^n - 1
        # 0 -> 000 -> []
        # 1 -> 001 -> [1]
        # 2 -> 010 -> [2]
        # ..
        # 7 -> 111 -> [1,2,3]
        result = []
        for i in range(1 << len(S)):
            subset = []
            for j in range(len(S)):
                # check whether the jth digit in i's binary representation is 1
                if (i & (1 << j)) != 0:
                    subset.append(S[j])
            result.append(subset)
        return result

    def subsets_3(self, S):
        self.results = []
        self.search(sorted(S), [], 0)
        return self.results

    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)

    def subsets_4(self, S):
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth + 1, i + 1, valuelist + [S[i]])

        S.sort()
        res = []
        dfs(0, 0, [])
        return res

if __name__ == '__main__':
    obj = Subsets()
    print(cProfile.run('obj.subsets([0])'))
