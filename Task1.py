from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Абстрактний клас Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Конкретний клас Car
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


# Конкретний клас Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


# Абстрактна фабрика
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")


# Фабрика для Європи
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")


# Головна функція
def main() -> None:
    us_factory: VehicleFactory = USVehicleFactory()
    eu_factory: VehicleFactory = EUVehicleFactory()

    vehicles = [
        us_factory.create_car("Ford", "Mustang"),
        us_factory.create_motorcycle("Harley-Davidson", "Sportster"),
        eu_factory.create_car("Volkswagen", "Golf"),
        eu_factory.create_motorcycle("Ducati", "Monster")
    ]

    for vehicle in vehicles:
        vehicle.start_engine()


if __name__ == "__main__":
    main()
