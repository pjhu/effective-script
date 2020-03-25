# -*- utf-8 -*-
"""
fifteenth
http://www.lintcode.com/en/problem/permutations/
"""
import cProfile
import itertools


class Permutations(object):
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
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

    def permute_2(self, nums):
        if nums is None:
            return []
        # not sorted is also ok
        nums = sorted(nums)
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                # stack[0,3,2] if index==2, 1 will not be find,
                # so use break, start 0 to find all index
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue
            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations

    def permute_tools_1(self, nums):
        l = []
        if nums is None:
            return l
        for i in itertools.permutations(nums, len(nums)):
            l.append(list(i))
        return l

    def permute_tools_2(self, iterable):
        # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
        # permutations(range(3)) --> 012 021 102 120 201 210
        def helper_tools(iterable):
            pool = tuple(iterable)
            n = len(pool)
            indices = list(range(n))
            cycles = list(range(n, 0, -1))
            yield list(pool[i] for i in indices)
            while n:
                for i in reversed(range(n)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i + 1:] + indices[i:i + 1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield list(pool[i] for i in indices)
                        break
                else:
                    return
        l = []
        for i in helper_tools(iterable):
            l.append(i)
        return l

    def permute_recursion_1(self, nums):
        alist = []
        result = []
        if not nums:
            return result
        self.helper_1(nums, alist, result)
        return result

    def helper_1(self, nums, alist, ret):
        if len(alist) == len(nums):
            ret.append([] + alist)
            return

        # 例:nums=[0,1,2,3].当i等于2时, 递归结束会产生一个permutation,
        # 此时alist=[0,1], 因为i等于2时, 递归调用for循环,
        # 加入alist加入3, 然后helper返回, 然后alist.pop,
        # 此时alist=[0,1,2], 并且i=2的递归循环结束, 然后进行i=3循环
        for i, item in enumerate(nums):
            if item not in alist:
                alist.append(item)
                self.helper_1(nums, alist, ret)
                alist.pop()

    # self complete
    def permute_recursion_2(self, nums):
        if nums is None:
            return []
        elif len(nums) <= 1:
            return [nums]

        result = []
        for i, item in enumerate(nums):
            for p in self.permute_recursion_2(nums[i + 1:] + nums[:i]):
                result.append([item] + p)

        return result

    def permute_recursion_3(self, nums):
        if nums is None:
            return []
        elif len(nums) <= 1:
            return [nums]

        result = []
        for i, item in enumerate(nums):
            for p in self.permute_recursion_3(nums[:i] + nums[i + 1:]):
                result.append(p + [item])

        return result


if __name__ == '__main__':
    obj = Permutations()
    print(cProfile.run('obj.permute_1([0,1,2,3])'))
