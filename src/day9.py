from typing import List
import itertools
from funcmeasure import measure

def read_steps(filename: str):
    with open(filename, 'r') as f:
        steps = f.read().rstrip('\n').split('\n')

    formatted_steps = []

    for step in steps:
        formatted_steps.append(int(step))

    return formatted_steps

def exc1(steps: List[int], low_i: int, high_i: int):
    preamble = steps[low_i:high_i]
    low_i += 1
    high_i += 1

    for numbers in itertools.combinations(preamble, 2):
        if sum(numbers) == steps[high_i-1]:
            return exc1(steps, low_i, high_i)

    return steps[high_i-1]

def exc2(steps: List[int], i: int, target: int):
    starting_i = i
    used_numbers = []
    total = 0

    while total < target:
        used_numbers.append(steps[i])
        total += steps[i]
        i += 1

        if total == target:
            return used_numbers

    starting_i += 1

    return exc2(steps, starting_i, target)

steps = read_steps('inputs/day9.txt')
exc1_result = exc1(steps, 0, 25) 
print(exc1_result) # Excercise 1

contigous_list = exc2(steps, 0, exc1_result)
min_num = min(contigous_list)
max_num = max(contigous_list)
print(min_num + max_num) # Exercise 2
