"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку
здійснюється за механізмом
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
from pprint import pprint

student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
student['Назар Степанов'] = {
        'Пошта': 'nazarstep@gmail.com',
        'Вік': 34,
        'Номер телефону': '+380957384855',
        'Середній бал': 96.3
}

top_students = []
for name, info in student.items():
    if info['Середній бал'] > 90:
        fullname = name.split()
        top_students.append({
            'First name': fullname[0],
            'Last name': fullname[1],
            'Average score': info['Середній бал']
        })

for students in top_students:
    print(f"{students['First name']} {students['Last name']} {students['Average score']}")

total = 0

for grade in student.values():
    total += grade['Середній бал']
count_student = (len(student))
avg_grade = total / count_student
print(f"Average students grade: {avg_grade}")

parents_number = '+380992349141'
for number in student.values():
    if not number['Номер телефону']:
        number['Номер телефону родичей'] = parents_number
pprint(student)

