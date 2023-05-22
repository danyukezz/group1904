import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycby0CR4jEusJwfovcdwZ-_JkyITtdoY4IU3gWpDL-t0tPZhy61oGZH9_g5ho7dnpQ-MgAg/exec'

response = requests.get(url)
inner_data = response.json()

total_cost = 0

for price in inner_data['data']:
    price_products = price.get('price')
    total_cost += price_products
pprint(total_cost)

total_cost_without_gluten = 0

for gluten in inner_data['data']:
    if gluten['gluten'] is False:
        price_products_without_gluten = gluten.get('price')
        total_cost_without_gluten += price_products_without_gluten
pprint(total_cost_without_gluten)
