# -*- utf-8 -*-
"""
fourteenth
http://www.lintcode.com/en/problem/first-position-of-target/
"""
import cProfile
import math


class FirstPositionOfTarget(object):
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binary_search(self, nums, target):
        return self.search_first(nums, target, 0, len(nums))

    def binary_search_exist(self, nums, target):
        return self.search_exist(nums, target, 0, len(nums))

    def search_exist(self, nums, target, start, end):
        if start < end:
            mid = math.floor((start + end - 1) / 2)
            if nums[mid] == target:
                return mid
            left = self.search_exist(nums, target, start, mid)
            if -1 != left:
                return left
            right = self.search_exist(nums, target, mid+1, end)
            if -1 != right:
                return right
            return -1
        else:
            return -1

    def search_first(self, nums, target, start, end):
        if start < end:
            mid = math.floor((start + end - 1) / 2)
            rst = [-1]
            if nums[mid] == target:
                rst[0] = mid
            rst.append(self.search_first(nums, target, start, mid))
            rst.append(self.search_first(nums, target, mid + 1, end))
            for i in rst[1:]:
                if rst[0] < 0:
                    rst[0] = i
                if 0 < i < rst[0]:
                    rst[0] = i
            return rst[0]
        else:
            return -1

if __name__ == '__main__':
    obj = FirstPositionOfTarget()
    print(cProfile.run("obj.binary_search([2,6,8,13,15,17,17,18,19,20], 15)"))
