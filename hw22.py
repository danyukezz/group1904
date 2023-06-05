import csv

with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as airports_file:
    reader = csv.DictReader(airports_file, fieldnames=['ident', 'type', 'name', 'elevation_ft', 'continent', 'iso_country', 'iso_region', 'municipality', 'gps_code', 'iata_code', 'local_code', 'coordinates'], delimiter=';')
    for airport in reader:
        if airport["iso_country"] == 'UA':
            print(airport["name"])
