from pprint import pprint

students = {
  'Ivan Petrov': {
    'Email': 'Ivan@gmail.com',
    'Age': 14,
    'Phone number': '+380987771221',
    'Average grade': 95.8
  },
  'Zhenya Kurich': {
    'Email': 'Geka@gmail.com',
    'Age': 16,
    'Phone number': None,
    'Average grade': 64.5
  },
  'Masha Kera': {
    'Email': 'Masha@gmail.com',
    'Age': 18,
    'Phone number': '+380986671221',
    'Average grade': 80
  },
}
students['Zhenya Kurich']['Age'] = 25
pprint(students)
pprint(len(students))