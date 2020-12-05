from typing import Dict, Iterator, List, Optional

def read_seats(filename: str) -> Iterator[str]:
    for seat in open(filename).readlines():
        yield seat

def calc_row(seat: str) -> int:
    low = 0
    high = 127

    for guide in seat[:7]:
        change = get_value_change(low, high)

        if guide == 'F':
            high -= change + 1

        if guide == 'B':
            low = change + low + 1

    return low

def calc_column(seat: str) -> int:
    low = 0
    high = 7
    
    for guide in seat[7:]:
        change = get_value_change(low, high)

        if guide == 'L':
            high -= change + 1

        if guide == 'R':
            low = change + low + 1
    
    return low

def get_seat_id(seat: str) -> int:
    row = calc_row(seat)
    col = calc_column(seat)

    return row * 8 + col

def get_value_change(low: int, high: int) -> int:
    return int((high - low) / 2)

def get_highest_seat(seats_path: str) -> int:
    highest_seat = 0

    for seat in read_seats(seats_path):
        seat_id = int(get_seat_id(seat))

        if seat_id > highest_seat:
            highest_seat = seat_id
    
    return highest_seat

def get_all_seats(seats_path: str) -> List[int]:
    seat_ids = []

    for seat in read_seats(seats_path):
        seat_id = int(get_seat_id(seat))
        seat_ids.append(seat_id)
    
    return sorted(seat_ids)

def get_missing_seat(seats_path: str) -> Optional[int]:
    last_seat = 5

    for seat_nr in get_all_seats(seats_path):
        if seat_nr - last_seat != 1:
            return seat_nr - 1

        last_seat = seat_nr

    return None

print(get_highest_seat('day04.txt')) # Exercise 1
print(get_missing_seat('day04.txt')) # Exercise 2