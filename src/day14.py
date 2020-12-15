from typing import List, Dict

def get_formatted_binary(num: int) -> str:
    return format(num, "036b")

def get_input(filename: str):
    with open(filename, 'r') as f:
        text = f.read().rstrip('\n')

    return text.split('\n')

def get_result(mask: str, val: str) -> int:
    result = ''
    for index, char in enumerate(mask):
        if char == 'X':
            char = val[index]
        
        result += char
    return int(result, 2)

def get_used_mems(text: List[str]) -> Dict[int, int]:
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
print('Exercise 1-', get_total_sum_of_used_mems(text)) # Exercise 1

# ------------ Exercise 2 ------------ #

def get_groups(text: List[str]) -> Dict[str, List[str]]:
    groups = {}

    for elem in text:
        if 'mask' in elem:
            latest_mask = elem.split('= ')[1]
            groups[latest_mask] = []
        else:
            groups[latest_mask].append(elem)

    return groups

def get_list_of_possible_mems(base_2_val: str) -> List[int]:
    base_10_val = int(base_2_val.replace('X', '0'), 2)
    base_10_vals = [base_10_val]

    for pos, char in enumerate(reversed(base_2_val)):
        if char == 'X':
            # multiple values
            base_10_x1_val = pow(2, pos)
            new_base_10_vals = []

            for previous_base_10_val in base_10_vals:
                new_base_10_vals.append(previous_base_10_val+base_10_x1_val)
            
            base_10_vals.extend(new_base_10_vals)

    return base_10_vals

def get_real_memory_value(mask: str, memory: str):
    result = ''
    for index, char in enumerate(mask):
        if char == '0':
            char = memory[index]
        
        result += char

    return result

def get_total_values(dict_of_groups: Dict[str, List[str]]) -> int:
    used_mems = {}
    for mask, values in dict_of_groups.items():
        for mem in values:
            memory = get_formatted_binary(int(mem.split('[')[1].split(']')[0]))
            real_mem = get_real_memory_value(mask, memory)
            possible_mems = get_list_of_possible_mems(real_mem)
            for possible_mem in possible_mems:
                used_mems[possible_mem] = int(mem.split('= ')[1])

    total = 0
    for value in used_mems.values():
        total += value
    
    return total

dict_of_groups = get_groups(text)
print('Exercise 2-', get_total_values(dict_of_groups)) # Exercise 2