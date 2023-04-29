name = input('Please enter your name -').title()
surname = input('Please enter your surname -').upper()
message = f"Здарова, {name} {surname}, а ти знав, що твоє імя складається з {len(name)} літер?"
print(message)