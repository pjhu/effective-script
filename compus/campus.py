# -*- utf-8 -*-
import os

from compus.IncorrectCommandFormatValidate import IncorrectCommandFormatValidate
from compus.InvalidNumberValidate import InvalidNumberValidate
from compus.MazeFormatErrorValidate import MazeFormatErrorValidate
from compus.NumberOutOfRangeValidate import NumberOutOfRangeValidate


def readCommandFromFile():
    input_file_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(input_file_path, "input.txt")) as f:
        data = f.readlines()
    return data


def outResult(result):
    [print(row) for row in result]


def validateCommand(command):
    if not InvalidNumberValidate.validate(''.join(command)):
        print("Invalid number format")
    if not NumberOutOfRangeValidate.validate(''.join(command)):
        print("Number out of range")
    if not IncorrectCommandFormatValidate.validate(command):
        print("Incorrect command format")
    if not MazeFormatErrorValidate.validate(command[1]):
        print("Maze format error")


def initMaze(maze_size):
    length, width = list(map(int, maze_size.rstrip('\n').split(' ')))
    maze = [['[R]' if (x % 2 == 1 & y % 2 == 1) else '[W]' for x in range(2 * width + 1)]
            for y in range(2 * length + 1)]
    return maze


def calculateConnectRoadPosition(start_x, start_y, end_x, end_y):
    x = start_x + end_x + 1
    y = start_y + end_y + 1
    return x, y


def connectedRoad(link):
    flat = []
    [flat.extend(l.split(',')) for l in link.split(' ')]
    int_link = list(map(int, flat))
    x, y = calculateConnectRoadPosition(int_link[0], int_link[1], int_link[2], int_link[3])
    return x, y


def updateMaze(command, maze):
    need_to_update_connected_road = [connectedRoad(link) for link in command]
    for x, y in need_to_update_connected_road:
        maze[x][y] = '[R]'
    return maze


def printMaze(command):
    validateCommand(command)
    init_maze = initMaze(command[0])
    road_connection = command[1].rstrip('\n').split(';')
    updated_maze = updateMaze(road_connection, init_maze)
    outResult(updated_maze)


if __name__ == "__main__":
    printMaze(readCommandFromFile())

