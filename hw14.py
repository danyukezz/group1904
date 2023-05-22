import requests
from pprint import pprint

url = 'https://dummyjson.com/users'
response = requests.get(url)
inner_data = response.json()

total_age = 0

for hair_color in inner_data['users']:
    if hair_color['color'] == 'Brown':
        for user in inner_data['users']:
            total_age += user['age']
            avg_age_people_with_brown_hair = total_age / (len(inner_data['users']))
        pprint(round(avg_age_people_with_brown_hair))
