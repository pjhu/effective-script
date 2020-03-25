# -*- coding: utf-8 -*-

import math
import random
import statistics
import sys
import itertools
from collections import Counter

print("tuple:", "=" * 100)
t = 12345, 54321, 'hello!'
x, y, z = t

print("numbers:", "=" * 100)
print("swap:")
a = 1
b = 3
a, b = b, a+b
print(a, b)

print("list:", "=" * 100)
print("sublist:")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[2:-1])

print("clear:")
letters[:] = []
del a[:]

print("Generator Expressions:")
print([(i + 'a') for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] if i > 'c'])
print([(x, y) for x in [1, 2, 3] for y in [1, 3, 4] if x != y])

print("unpack the arguments out of a list or tuple:")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
print(list(zip(*matrix)))

print((1, 2) < (1, 2, -1))

print("set:", "=" * 100)
a = set("abracadabra")
b = set("alacazam")
print(a-b, a | b, a & b)

print("dict:", "=" * 100)
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


print("Statements:", "=" * 100)
for i in range(0, 10, 3):
    print(i)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for index, item in enumerate(letters):
    print(index, item)
else:
    print('===========')

print("module:", "=" * 100)
print(dir(sys))


print("function:", "=" * 100)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
print(divide(2, 1))
print(divide(2, 0))
print(divide("2", "1"))

print("Iterator:", "=" * 100)
a = "abc"
it = iter(a)
next(it)

print("Generator:", "=" * 100)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('Generator'):
    print(char)

print("import itertools:", "=" * 100)
print(list(itertools.permutations([1, 2, 3, 4])))
itertools.combinations([1,2,3])


print("Mathematics:", "=" * 100)
print(math.cos(math.pi / 4))


print(random.choice(['apple', 'pear', 'banana']))
print(statistics.mean([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]))

print(".".join(["1", "2", "3"]))

temp = math.cos
for i in range(0,10):
    print(temp(i))

print("counter:", "=" * 100)
some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
print(Counter(some_data))
print(Counter(some_data).elements())


print("cProfile", "argsparse", "cPickle", "JSON", "traceback获取栈信息", "logging")

