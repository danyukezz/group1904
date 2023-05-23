def joke(value):
    # value = input('Enter your number >>> ')
    if value == 1:
        return 'Анекдот про школу'
    if value == 2:
        return 'Анекдот про рибака'
    if value:
        return 'Анекдот про кота'
print(joke(1))

def perimeter() -> float:
    perimeter_rectangle = (width + height) * 2
    floated_perimeter_rectangle = float(perimeter_rectangle)
    return floated_perimeter_rectangle
width = 10
height = 20
print(perimeter())


def string(letter):
    bad_letters = ['Ї', 'ї', 'ж', 'Ж']
    for letters in bad_letters:
        letter = letter.replace(letters, '')
    return letter
print(string('хижак та їжак та їжа'))

def remove_letters(letter, letters_1):
    for twice_letter in letters_1:
        letter = letter.replace(twice_letter.lower(), '')
        letter = letter.replace(twice_letter.upper(), '')
    return letter
print(remove_letters("хижак", "вікно"))
