from typing import List, Tuple
import copy

def read_steps(filename: str):
    with open(filename, 'r') as f:
        steps = f.read().rstrip('\n').split('\n')

    return steps
    
def format_steps(filename:str):
    formatted_steps = []

    for opr in read_steps(filename):
        command, number = opr.split(' ')
        formatted_steps.append((command, int(number)))
    
    return formatted_steps

def get_acc_before_repeated_steps(filename: str) -> int:
    used_indexes = []
    index = 0
    acc = 0
    steps = format_steps(filename)

    while index not in used_indexes:
        used_indexes.append(index)
        command, number = steps[index]

        if command == 'acc':
            acc += number  
        elif command == 'jmp':
            index += number
            
            continue

        index += 1

    return acc

def get_final_acc(steps: List[Tuple[str, int]]) -> int:
    used_indexes = []
    index = 0
    last_index = 0
    acc = 0
    len_steps = len(steps)

    while index < len_steps:
        if index in used_indexes:
            f_command, f_number = steps[last_index]
            steps[last_index] = ('jmp' if f_command == 'nop' else 'nop', f_number)
            print(steps[last_index])

            return get_final_acc(steps)

        used_indexes.append(index)
        command, number = steps[index]
        last_index = index

        if command == 'acc':
            acc += number   
        elif command == 'jmp':
            index += number
            
            continue
        
        index += 1

    return acc
    
print(get_acc_before_repeated_steps('inputs/day8.txt')) # Exercise 1
# print(get_final_acc(format_steps('inputs/day8.txt')))
# Exercise 2 - coming soon 
