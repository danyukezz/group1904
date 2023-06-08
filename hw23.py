from datetime import datetime
class Car:
    def __init__(self, issue_year: int, manufacturer: str, model: str, gas: float) -> None:
        self.__issue_year = issue_year
        self.__manufacturer = manufacturer
        self.__model = model
        self.gas = gas
        self._mileage = 0

    def __str__(self):
        return f"Car: {self.__issue_year}, {self.__manufacturer}, {self.__model}, {self.gas}, {self.mileage}"

    @property
    def issue(self):
        issue = datetime.today().year - self.__issue_year
        return issue

    def mileage(self):
        return self._mileage

car1 = Car(2021, 'BMW', 'M5', 5.5)
car1.mileage = 40000
car2 = Car(2019, 'Mercedes', 'CLS', 6.1)
car2.mileage = 10000
car3 = Car(2019, 'Audi', 'Q8', 7.8)
car3.mileage = 35600
print(car1)
print(car2)
print(car3)