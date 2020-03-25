# -*- utf-8 -*-
import os
import re


class NumberOutOfRangeValidate:

    @staticmethod
    def validate(command):
        elements = list(map(int, re.split(r'[;, \n]', command.rstrip())))
        return [0 <= element < elements[0] for element in elements[2:]].count(False) == 0


if __name__ == '__main__':
    input_file_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(input_file_path, "input.txt")) as f:
        data = f.read()
    print(NumberOutOfRangeValidate.validate(''.join(data)))
