from multi_fuel_dispenser.fuel import Fuel


class Dispenser:
    def __init__(self):
        self.fuels = {}
        self.transactions = []


    def add_fuel(self, fuel_name:str, fuel:Fuel):
        fuel_name = fuel_name.lower()

        if fuel_name in self.fuels:
            raise ValueError("Fuel already exists.")
        self.fuels[fuel_name] = fuel

    def get_fuel(self,fuel_name:str):
        fuel_name = self.__validate_fuel(fuel_name)

        return self.fuels[fuel_name]

    def update_price(self, fuel_name:str, price:float):

        if price < 1:
            raise ValueError ("Price can not be updated to be less than 1.")

        fuel_name = self.__validate_fuel(fuel_name)
        fuel = self.get_fuel(fuel_name)
        fuel.set_price_per_liter(price)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_all_fuels(self):
        return list(self.fuels.keys())


    def restock_fuel(self, fuel_name:str, liter:float):

        if liter < 1:
            raise ValueError ("Invalid liter,Liter must be greater than 1.")

        fuel_name = self.__validate_fuel(fuel_name)
        fuel = self.fuels[fuel_name]

        new_stock = fuel.get_quantity() + liter
        fuel.set_quantity(new_stock)
        # self.fuels[fuel_name].set_quantity(new_stock)

    def __validate_fuel(self, fuel_name: str):
        fuel_name = fuel_name.lower()

        if fuel_name not in self.fuels:
            raise ValueError("The company does not currently sell this fuel.")

        return fuel_name