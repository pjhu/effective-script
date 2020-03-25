# -*- utf-8 -*-
"""
fifteenth
http://www.lintcode.com/en/problem/permutations/
"""
import cProfile


class PermutationsUnique(object):
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute_unique(self, nums):
        return self.permute_c_plus_plus(nums)

    def permute_c_plus_plus(self, nums):
        """
        C++ std::next_permutation Implementation Explanation
        http://stackoverflow.com/questions/11483060/stdnext-permutation-implementation-explanation
        ...
        1 4 3 2
        2 1 3 4
        ...
        2 4 3 1
        3 1 2 4
        ...
        We see that when everything to the right of a digit is in descending order,
        we find the next largest digit and put it in front
        and then put the remaining digits in ascending order
        """
        if nums is None:
            return [[]]
        elif len(nums) <= 1:
            return [nums]

        # sort nums first
        nums.sort()

        result = []
        while True:
            result.append([] + nums)
            # step1: find nums[i] < nums[i + 1], Loop backwards
            i = 0
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    break
                elif i == 0:
                    return result
            # step2: find nums[i] < nums[j], Loop backwards
            j = 0
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    break
            # step3: swap betwenn nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # step4: reverse between [i + 1, n - 1]
            nums[i + 1:len(nums)] = nums[len(nums) - 1:i:-1]
        return result

    def permute_unique_2(self, nums):
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i + 1:])

        if nums is None:
            return []
        result = []
        _permute(result, [], sorted(nums))
        return result


if __name__ == '__main__':
    obj = PermutationsUnique()
    print(cProfile.run('obj.permute_1([0,1,2,3])'))
