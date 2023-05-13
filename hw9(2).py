surnames = input(str('Enter your surname >>> ')).split(", ")
surnames_result = []
for elements in surnames:
    if elements.istitle():
        surnames_result.sort()
        surnames_result.append(elements)
print(surnames_result)






