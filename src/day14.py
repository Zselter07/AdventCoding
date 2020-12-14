from typing import List, Dict

def get_formatted_binary(num: int) -> str:
    return format(num, "036b")

def get_input(filename: str):
    with open(filename, 'r') as f:
        text = f.read().rstrip('\n')

    return text.split('\n')

def get_result(mask: str, val: str):
    result = ''
    for index, char in enumerate(mask):
        if char == 'X':
            char = val[index]
        
        result += char
    return int(result, 2)

def get_used_mems(text: List[str]):
    used_mems = {}

    for elem in text:
        if 'mask' not in elem:
            used_mems[int(elem.split('[')[1].split(']')[0])] = get_result(mask, get_formatted_binary(int(elem.split('= ')[1])))
        else:
            mask = elem.split('= ')[1]

    return used_mems

def get_total_sum_of_used_mems(text: List[str]) -> int:
    total = 0
    for sums in get_used_mems(text).values():
        total += sums
    
    return total

text = get_input('inputs/day14.txt')
print(get_total_sum_of_used_mems(text)) # Exercise 1
