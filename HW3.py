from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def provide_info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, house):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, availability_money, salary, own_home: list):
        self.name = name
        self.age = age
        self.availability_money = availability_money
        self.salary = salary
        self.own_home = own_home

    def provide_info(self):
        print(f' Info about person:\n'
              f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Money availability: {self.availability_money}\n'
              f'Salary: {self.salary}\n')

    def make_money(self):
        print(f'Sum of money is {self.availability_money}')
        self.availability_money += self.salary
        print(f'After receiving: {self.availability_money}')

    def buy_house(self, house):
        if  self.availability_money < house.cost:
            print(f"You can`t bought this house.")
        else:
            self.availability_money -= house.cost
            self.own_home.append(house)
            print(f"You can bought a house.")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost


class SmallTypicalHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(area, cost)


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, age, houses: list):
        self.name = name
        self.age = age
        self.houses = houses

    def provide_info_realtor(self):
        print(f'Info about realtor:\n'
              f'Name realtor: {self.name}\n'
              f'Age realtor: {self.age}\n'              
              f'You can buy such houses for now as:')
        for home in self.houses:
            print(f'The area of house is {home.area}, it costs {home.cost}')

    def give_discount(self, house):
        print(f'Realtor would like to propose you a discount')
        if house in self.houses:
            house.cost -= house.cost / 100 * random.randint(1, 50)
        print(f'Now the price of this house is {house.cost}')

    @staticmethod
    def steal_money(person):
        probability = random.randint(1, 10)
        if probability == 1:
            person.availability_money = max(person.availability_money - random.randint(100, 10000), 0)
        print(f"Sorrow! The realtor steals your money!")

if __name__ == "__main__":
    house1 = House(43, 44000)
    house2 = House(75, 80000)
    house3 = House(88, 98000)

    person1 = Person("Lucy", 28, 40000, 20000, [])
    person1.provide_info()
    person1.make_money()

    realtor1 = Realtor('Din', 38, [house1, house2, house3])
    realtor1.provide_info_realtor()
    realtor1.give_discount(house3)
    person1.buy_house(house3)
    realtor1.steal_money(person1)
