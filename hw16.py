def kilometers_to_miles(kilometers: float) -> float:
    if kilometers < 0:
        raise ValueError('Negative miles is unacceptable')
    miles = kilometers * 1.60934
    return miles

def get_unique_letters(data) -> tuple:
    unique_elements = sorted(set(data), key=int)
    return tuple(unique_elements)