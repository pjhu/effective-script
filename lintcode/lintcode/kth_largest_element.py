# -*- utf-8 -*-
"""
fifth
http://www.lintcode.com/en/problem/kth-largest-element/

Find K-th largest element in an array.
"""
import profile


class KthLargestElement(object):
    def kth_largest_element(self, k, A):
        A.sort()
        return A[-k]

    def kth_largest_element_2(self, k, A):
        rst = self.helper(A, 0, len(A) - 1, len(A) - k)
        return rst

    def helper(self, nums, left, right, k):
        if left == right:
            return nums[left]
        i = left
        j = right
        pivot = nums[(i + j) // 2]
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if left + k <= j:
            return self.helper(nums, left, j, k)
        if left + k < i:
            return nums[left + k]
            # return nums[i - 1]
        return self.helper(nums, i, right, k - (i - left))

    def kth_largest_element_3(self, k, A):
        rst = self.helper_2(A, 0, len(A) - 1, len(A) - k)
        return rst

    def helper_2(self, nums, l, r, k):
        if l == r:
            return nums[l]
        position = self.partition(nums, l, r)
        if position + 1 == k:
            return nums[position]
        elif position + 1 < k:
            return self.helper_2(nums, position + 1, r, k)
        else:
            return self.helper_2(nums, l, position - 1, k)

    def partition(self, nums, l, r):
        left = l
        right = r
        pivot = nums[left]

        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right];
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        return left

if __name__ == '__main__':
    obj = KthLargestElement()
    print(profile.run('obj.kth_largest_element_2(2, [1,2])'))

