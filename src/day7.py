from typing import List, Dict
import copy

def read_rules(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        text = f.read().rstrip('\n')
    
    return text.split('\n')

def format_rules(filename: str) -> Dict[str, Dict[str, int]]:
    rules = {}
    for rule in read_rules('inputs/day7.txt'):
        d = {}
        key, value = rule.rstrip('.').split(' contain ')
        key = key.split(" bag")[0]
        values = [value.split(" bag")[0] for value in value.split(', ')]
        
        if 'no other' in value:
            rules[key] = {}

            continue
        
        for value in values:
            val = int(value.split(' ')[0])
            k = value[2:]
            d[k] = val

        rules[key] = d

    return rules

def count_possible_bag_types(rules: Dict[str, Dict[str, int]], bag_names: List[str], result: List[str]):
    start_result = copy.deepcopy(result)
    next_bag_names = []

    for curr_bag, curr_sub_bags in rules.items():
        for bag_name in bag_names:
            if bag_name in list(curr_sub_bags.keys()) and curr_bag not in result:
                result.append(curr_bag)
                next_bag_names.append(curr_bag)

                break

    if len(result) > len(start_result):
        count_possible_bag_types(rules, next_bag_names, result)
    
    return result

def calc_possible_bags(rules: Dict[str, Dict[str, int]]) -> int:
    return len(count_possible_bag_types(rules, ['shiny gold'], []))

def calc_bag_count(rules: Dict[str, Dict[str, int]], bag_color: str) -> int:
    count = 0

    for bag_name, bag_number in rules[bag_color].items():
        count += bag_number + bag_number * calc_bag_count(rules, bag_name)

    return count

rules = format_rules('inputs/day7.txt')

print(calc_possible_bags(rules)) # Exercise 1
print(calc_bag_count(rules, 'shiny gold')) # Exercise 2