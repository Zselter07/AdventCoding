from typing import List, Dict, Optional

def read_input(filename: str):
    with open(filename, 'r') as f:
        steps = f.read().rstrip('\n').split('\n')

    return [list(step) for step in steps]

def get_neighbours(index: int, current_line: List[str], previous_line: Optional[List[str]]=None, next_line: Optional[List[str]]=None) -> List[str]:
    negihbours = []
    
    if index == 0:
        negihbours.append(current_line[index+1])
        if previous_line:
            negihbours.extend([previous_line[index], previous_line[index+1]])
        if next_line:
            negihbours.extend([next_line[index], next_line[index+1]])
    elif index == len(current_line) - 1:
        negihbours.append(current_line[index-1])
        if previous_line:
            negihbours.extend([previous_line[index], previous_line[index-1]])
        if next_line:
            negihbours.extend([next_line[index], next_line[index-1]])
    else:
        negihbours.extend([current_line[index+1], current_line[index-1]])
        if previous_line:
            negihbours.extend([previous_line[index], previous_line[index-1], previous_line[index+1]])
        if next_line:
            negihbours.extend([next_line[index], next_line[index-1], next_line[index+1]])

    return negihbours

def get_new_arrangement(seats: List[List[str]]) -> Optional[List[List[str]]]:
    import copy

    new_seats = []
    seats_copy = copy.deepcopy(seats)

    for big_i, line in enumerate(seats):
        new_line = []
        for i, seat in enumerate(line):
            if seat == '.':
                new_line.append('.')
                continue

            if big_i == 0:
                neighbours=get_neighbours(i, current_line=line, next_line=seats[big_i+1])
            elif big_i == len(seats)-1:
                neighbours = get_neighbours(i, current_line=line, previous_line=seats[big_i-1])
            else:
                neighbours = get_neighbours(i, current_line=line, previous_line=seats[big_i-1], next_line=seats[big_i+1])
            
            if seat == 'L':
                if neighbours.count('#') == 0:
                    new_line.append('#')
                else:
                    new_line.append('L')
            elif seat == '#':
                if neighbours.count('#') >= 4:
                    new_line.append('L')
                else:
                    new_line.append('#')

        new_seats.append(new_line)

    if new_seats == seats_copy:
        return new_seats
    
    return get_new_arrangement(new_seats)

def get_total_occupied_seats(seats: List[List[str]]) -> int:
    total = 0
    final_groups = get_new_arrangement(seats)

    for line in final_groups:
        for seat in line:
            if seat == '#':
                total += 1
    
    return total

seats = read_input('inputs/day11.txt')
print(get_total_occupied_seats(seats)) # Exercise 1