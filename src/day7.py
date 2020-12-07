from typing import List, Dict
import copy

def read_rules(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        text = f.read().rstrip('\n')
    
    return text.split('\n')

def format_rules(filename: str) -> Dict[str, List[str]]:
    rules = {}
    for rule in read_rules('inputs/day7.txt'):
        key, value = rule.rstrip('.').split(' contain ')
        values = [value.split(" bag")[0] for value in value.split(', ')]
        
        if 'no other' in value:
            continue

        values = [(int(value.split(' ')[0]), value[2:]) for value in values]
        rules[key.split(" bag")[0]] = values

    return rules

def count_possible_bag_types(rules: Dict[str, List[str]], bag_names: List[str], result: List[str]):
    start_result = copy.deepcopy(result)
    next_bag_names = []

    for curr_bag, curr_sub_bags in rules.items():
        for bag_name in bag_names:
            if any(bag_name in substr for substr in curr_sub_bags) and curr_bag not in result:
                result.append(curr_bag)
                next_bag_names.append(curr_bag)

                break

    if len(result) > len(start_result):
        count_possible_bag_types(rules, next_bag_names, result)
    
    return result

def exercise1(filename: str) -> int:
    rules = format_rules(filename)

    return len(count_possible_bag_types(rules, ['shiny gold'], []))

print(exercise1('inputs/day7.txt')) # Exercise 1