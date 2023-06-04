import requests
url = "https://ichef.bbci.co.uk/news/800/cpsprodpb/6C7E/production/_98847772_60e395f3-f84e-4215-8626-0b977b85e838.jpg"
response = requests.get(url)
with open('file.png', "wb") as file:
    file.write(response.content)

