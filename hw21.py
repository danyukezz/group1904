import requests
url = "https://upload.wikimedia.org/wikipedia/commons/1/19/Europ%C3%A4ischer_Ziesel_in_Hockstellung.jpg"
response = requests.get(url)
with open('file.png', "wb") as file:
    file.write(response.content)

