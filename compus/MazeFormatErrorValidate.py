# -*- utf-8 -*-
import os
import re


class MazeFormatErrorValidate:

    @staticmethod
    def validate(command):
        elements = list(map(int, re.split(r'[; , ]', command.rstrip())))
        return [(abs(elements[index] - elements[index+2]) + abs(elements[index+1] - elements[index+3])) != 1
                for index in range(0, len(elements), 4)].count(False) > 0


if __name__ == '__main__':
    input_file_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(input_file_path, "input.txt")) as f:
        data = f.readlines()
    print(MazeFormatErrorValidate.validate(data[1]))
