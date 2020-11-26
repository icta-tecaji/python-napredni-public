def print_events(values):
    for val in values:
        is_even = ((val % 2) == 0)
        if is_even:
            print(f'Found even value {val}')
