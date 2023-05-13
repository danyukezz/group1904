from decimal import Decimal

temperature_celsius = float(input('Input temperature degree >>> '))
temperature_fahrenheit = (9/5 * temperature_celsius + 32)
temperature_fahrenheit_rounded = Decimal(temperature_fahrenheit)
print(round(temperature_fahrenheit_rounded, 1))