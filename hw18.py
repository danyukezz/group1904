def get_number(number):
    if number < 1:
        raise ValueError
    else:
        return [number + i for i in(range(10))]
print(get_number(3))
