letters = input('Type your string >>> ')
letters_result = []
for element in letters:
    if element.isupper():
        letters_result.append(element)
print(letters_result)