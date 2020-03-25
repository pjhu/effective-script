# -*- utf-8 -*-
import os
import re


class InvalidNumberValidate:

    @staticmethod
    def validate(command):
        elements = re.split(r'[;, \n]', command.rstrip())
        return [element.isdigit() for element in elements].count(False) == 0


if __name__ == '__main__':
    input_file_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(input_file_path, "input.txt")) as f:
        data = f.readlines()
    print(InvalidNumberValidate.validate(''.join(data)))
