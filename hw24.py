from abc import ABC, abstractmethod


class TransportVehicle(ABC):
    def __init__(self, model: str, tank_volume: int, gas_rest: float, speed: int, mileage: int):
        self.model = model
        self.tank_volume = tank_volume
        self.gas_rest = gas_rest
        self.speed = speed
        self.mileage = mileage

    @abstractmethod
    def __str__(self):
        pass

    def refuel(self):
        added_fuel = self.tank_volume - self.gas_rest
        self.gas_rest += added_fuel

    def fuel_transfer(self, other):
        if other.gas_rest > 0 and self.gas_rest < self.tank_volume:
            transferred_fuel = other.gas_rest
            self.gas_rest += other.gas_rest
            other.gas_rest -= transferred_fuel
        else:
            raise ValueError
        

class Car(TransportVehicle):
    def __init__(self, model: str, tank_volume: int, gas_rest: int, speed: int, mileage: int, passengers_amount: int,
                 airbag: bool):
        super().__init__(model, tank_volume, gas_rest, speed, mileage)
        self.passengers_amount = passengers_amount
        self.airbag = airbag

    def __str__(self):
        return f"I am a car: {self.model}, {self.tank_volume}, {self.gas_rest}, {self.speed}, {self.mileage}, {self.passengers_amount}, {self.airbag} "


class Bike(TransportVehicle):
    def __init__(self, model: str, tank_volume: int, gas_rest: int, speed: int, mileage: int, lulka: bool):
        super().__init__(model, tank_volume, gas_rest, speed, mileage)
        self.lulka = lulka

    def __str__(self):
        return f"I am a bike: {self.model}, {self.tank_volume}, {self.gas_rest}, {self.speed}, {self.mileage}, {self.lulka} "


car = Car(model="BMW", tank_volume=20, gas_rest=10, speed=120, mileage=10000, passengers_amount=4, airbag=True)
bike = Bike(model="Honda", tank_volume=7, gas_rest=3, speed=100, mileage=5000, lulka=True)

print(car)
print(bike)
