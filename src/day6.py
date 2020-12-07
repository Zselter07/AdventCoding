from typing import List

def read_answers(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        text = f.read().rstrip('\n')
    
    answers = [answer.split('\n') for answer in text.split('\n\n')]
    
    return answers

def calc_any(filename: str):
    total = 0

    for group in read_answers(filename):
        cleaned_group = []
        for person in group:
            for char in person:
                if char not in cleaned_group:
                    cleaned_group.append(char)
        
        total += len(set(cleaned_group))

    return total

def calc_every(filename: str):
    total = 0

    for group in read_answers(filename):
        chars = [list(person) for person in group]
        result = set(chars[0])
        for s in chars[1:]:
            result.intersection_update(s)
        
        total += len(result)

    return total

print(calc_any('inputs/day6.txt')) # Exercise 1
print(calc_every('inputs/day6.txt')) # Exercise 2
