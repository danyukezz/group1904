name_cities = set(input('Input cities that you visited for last 10 years >>> ').title().split(", "))
future_cities = set(input('Input cities that you would like to visit in the future 10 years >>> ').title().split(", "))

liked_cities = name_cities & future_cities
common_cities = name_cities ^ future_cities

print(f"You liked this cities >>> {liked_cities}")
print(f"You are open for new adventures >>> {common_cities}")
