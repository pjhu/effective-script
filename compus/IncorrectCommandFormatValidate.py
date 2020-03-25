# -*- utf-8 -*-
import os
import re


class IncorrectCommandFormatValidate:

    @staticmethod
    def validate(command):
        first_line = list(map(int, command[0].rstrip().split()))
        if len(first_line) != 2 or first_line[0] != first_line[1]:
            return False
        if [len(sicolon.split(' ')) == 2 for sicolon in command[1].rstrip().split(';')].count(False) > 0:
            return False
        if [len(element.split(',')) == 2 for element in re.split('[; ]', command[1])].count(False) > 0:
            return False
        return True

if __name__ == '__main__':
    input_file_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(input_file_path, "input.txt")) as f:
        data = f.readlines()
    print(IncorrectCommandFormatValidate.validate(data))
