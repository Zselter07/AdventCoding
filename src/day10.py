from typing import List

def read_steps(filename: str):
    with open(filename, 'r') as f:
        steps = f.read().rstrip('\n').split('\n')

    formatted_steps = []

    for step in steps:
        formatted_steps.append(int(step))

    return formatted_steps

def get_differences(adapters: List[int]):
    adapters = sorted(adapters)
    len_list = len(adapters)
    last_i = 0
    i = 1

    if adapters[0] == 1:
        ones_diff = 1
        threes_diff = 1
    elif adapters[0] == 3:
        ones_diff = 0
        threes_diff = 2

    while i < len_list:
        if adapters[i] - adapters[last_i] == 1:
            ones_diff += 1
        elif adapters[i] - adapters[last_i] == 3:
            threes_diff += 1

        i += 1
        last_i += 1

    return ones_diff * threes_diff

adapters = read_steps('inputs/day10.txt')
print(get_differences(adapters)) # Exercise 1