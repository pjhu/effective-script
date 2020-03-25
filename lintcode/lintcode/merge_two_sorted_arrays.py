# -*- utf-8 -*-
"""
sixth
http://www.lintcode.com/en/problem/merge-two-sorted-arrays/

Merge two given sorted integer array A and B into a new sorted integer array.
"""
import profile


class MergeTwoSortedArrays(object):
    # @param A and B: sorted integer array A and B.
    # @return: A new sorted integer array
    def merge_two_sorted_arrays(self, A, B):
        l = []
        j = 0
        for i in range(len(A)):
            while j < len(B) and A[i] > B[j]:
                l.append(B[j])
                j += 1
            l.append(A[i])
        if i < len(A) - 1:
            l.extend(A[i:])
        if j < len(B):
            l.extend(B[j:])
        return l

if __name__ == '__main__':
    obj = MergeTwoSortedArrays()
    print(profile.run('obj.merge_two_sorted_arrays([1, 3, 5], [4])'))
