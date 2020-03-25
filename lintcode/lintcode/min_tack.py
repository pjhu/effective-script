# -*- utf-8 -*-
"""
twelfth
http://www.lintcode.com/en/problem/min-stack/
"""
import profile


class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.__min = []
        self.__stack = []

    def push(self, number):
        # write yout code here
        if not self.__min or self.__min[-1] >= number:
            self.__min.append(number)
        self.__stack.append(number)

    def pop(self):
        # pop and return the top item in stack
        if self.__min[-1] == self.__stack[-1]:
            self.__min.pop()
        return self.__stack.pop()

    def min(self):
        # return the minimum number in stack
        # min(self.__stack)
        return self.__min[-1]

if __name__ == '__main__':
    obj = MinStack()
    obj.push(1), obj.pop(), obj.push(2), obj.push(3), obj.min(), obj.push(1), obj.min()
