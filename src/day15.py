import copy

def get_numbers():
    n = 7
    puzzle_input = [2,1,10,11,0,6]

    while n != 2021:
        iterator = copy.deepcopy(puzzle_input)
        last_indexes = []

        for index, number in enumerate(iterator):
            if number == puzzle_input[-1]:
                last_indexes.append(index)
        
        n += 1
        if last_indexes is None or len(last_indexes) == 1:
            puzzle_input.append(0)
        else:    
            last_indexes = sorted(last_indexes, reverse=True)
            puzzle_input.append(last_indexes[0]-last_indexes[1])

    return puzzle_input

print(get_numbers()) # Exercise 1

