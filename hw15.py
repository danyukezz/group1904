def joke(value):
    # value = input('Enter your number >>> ')
    if value == 1:
        return 'Анекдот про школу'
    if value == 2:
        return 'Анекдот про рибака'
    if value:
        return 'Анекдот про кота'
print(joke(1))

def perimeter():
    perimeter_rectangle = (width + height) * 2
    floated_perimeter_rectangle = float(perimeter_rectangle)
    return floated_perimeter_rectangle

width = 10
height = 20
print(perimeter())


def string(letter):
    bad_letters = letter.replace('ї', '').replace('ж', '').replace('Ї', '').replace('Ж', '')
    return bad_letters
print(string('хижак та їжак та їжа'))