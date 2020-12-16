from typing import List, Dict, Tuple, Optional

def read_input(filename: str) -> List[Tuple[str, int]]:
    with open(filename, 'r') as f:
        steps = f.read().rstrip('\n')
    
    steps = steps.split('\n')
    steps = [(step[0], int(step[1:])) for step in steps]

    return steps

def move(inputs: List[Tuple[str, int]]):
    east = 0
    north = 0
    ship_dir = 'E'
    for step in inputs:
        direction, number = step

        if direction == 'N':
            north += number
        elif direction == 'S':
            north -= number
        elif direction == 'E':
            east += number
        elif direction == 'W':
            east -= number
        elif direction == 'F':
            if ship_dir == 'N':
                north += number
            elif ship_dir == 'S':
                north -= number
            elif ship_dir == 'E':
                east += number
            elif ship_dir == 'W':
                east -= number
        elif direction == 'R':
            if number == 90:
                if ship_dir == 'E':
                    ship_dir = 'S'
                elif ship_dir == 'S':
                    ship_dir = 'W'
                elif ship_dir == 'W':
                    ship_dir = 'N'
                elif ship_dir == 'N':
                    ship_dir = 'E'
            elif number == 180:
                if ship_dir == 'E':
                    ship_dir = 'W'
                elif ship_dir == 'S':
                    ship_dir = 'N'
                elif ship_dir == 'W':
                    ship_dir = 'E'
                elif ship_dir == 'N':
                    ship_dir = 'S'
            elif number == 270:
                if ship_dir == 'E':
                    ship_dir = 'N'
                elif ship_dir == 'S':
                    ship_dir = 'E'
                elif ship_dir == 'W':
                    ship_dir = 'S'
                elif ship_dir == 'N':
                    ship_dir = 'W'
        elif direction == 'L':
            if number == 90:
                if ship_dir == 'E':
                    ship_dir = 'N'
                elif ship_dir == 'S':
                    ship_dir = 'E'
                elif ship_dir == 'W':
                    ship_dir = 'S'
                elif ship_dir == 'N':
                    ship_dir = 'W'
            elif number == 180:
                if ship_dir == 'E':
                    ship_dir = 'W'
                elif ship_dir == 'S':
                    ship_dir = 'N'
                elif ship_dir == 'W':
                    ship_dir = 'E'
                elif ship_dir == 'N':
                    ship_dir = 'S'
            elif number == 270:
                if ship_dir == 'E':
                    ship_dir = 'S'
                elif ship_dir == 'S':
                    ship_dir = 'W'
                elif ship_dir == 'W':
                    ship_dir = 'N'
                elif ship_dir == 'N':
                    ship_dir = 'E'
    
    return abs(east) + abs(north)

# Very ugly, don't do it like this

inputs = read_input('inputs/day12.txt')
print(move(inputs))


