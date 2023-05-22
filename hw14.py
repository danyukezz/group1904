import requests
from pprint import pprint

url = 'https://dummyjson.com/users'
response = requests.get(url)
inner_data = response.json()

men_with_brown_hair = [user['age'] for user in inner_data['users'] if user['gender'] == 'male' and user['hair']['color'] == 'Brown']
if men_with_brown_hair:
    average_age_men_with_brown_hair = sum(men_with_brown_hair) / len(men_with_brown_hair)
    pprint(f"Average age of men with brown hair: {average_age_men_with_brown_hair}")

louisville_citizen = [user for user in inner_data['users'] if user['address']['city'] == 'Louisville']
if louisville_citizen:
    for user in louisville_citizen:
    pprint(user['firstName'], user['lastName'])