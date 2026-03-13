from datetime import datetime
from multi_fuel_dispenser.dispenser import Dispenser
from multi_fuel_dispenser.fuel import Fuel


# harshard, fibonacci,triangular

class FuelAttendant:

    # dispenser = Dispenser()

    def __init__(self, name: str, dispenser: Dispenser):
        self.name = name
        self.__dispenser = dispenser


    def add_new_fuel(self,fuel_name,price_per_liter,quantity):
        fuel = Fuel(fuel_name,price_per_liter,quantity)
        self.__dispenser.add_fuel(fuel_name, fuel)

    def sell_fuel_by_liter(self,fuel_name:str,liter:float):
        fuel = self.__dispenser.get_fuel(fuel_name.lower())

        if liter > fuel.get_quantity():
            raise ValueError("Not enough fuel in stock.")

        amount = liter *fuel.get_price_per_liter()
        remaining_quantity = fuel.get_quantity() - liter
        fuel.set_quantity(remaining_quantity)
        transaction = f"Fuel Type: {fuel_name} | Amount Bought: {amount} | Liters Bought: {liter} | Time & Date :{self.__dispenser.formatted_date}"
        receipt = self.generate_receipt(fuel_name,amount,liter)
        self.__dispenser.add_transaction(transaction)

        return receipt

    def sell_fuel_by_amount(self,fuel_name,amount:float):
        fuel = self.__dispenser.get_fuel(fuel_name.lower())
        liter_bought = amount / fuel.get_price_per_liter()
        remaining_quantity = fuel.get_quantity() - liter_bought
        fuel.set_quantity(remaining_quantity)

        transaction = f"Fuel Type: {fuel_name} | Amount Bought: {amount} | Liters Bought: {liter_bought} | Time & Date :{self.__dispenser.formatted_date}"
        receipt = self.generate_receipt(fuel_name,amount,liter_bought)
        self.__dispenser.add_transaction(transaction)

        return receipt


    def restock_fuel(self,fuel_name:str,liter:float):
        self.__dispenser.restock_fuel(fuel_name, liter)

    def update_price(self,fuel_name:str,amount:float):
         self.__dispenser.update_price(fuel_name, amount)


    # def generate_receipt (self, fuel_name: str, amount:float, liters:float):
    #     transaction = f"Fuel Type: {fuel_name} Amount Bought: {amount} Liters Bought: {liters}"
    #     return transaction

    def generate_receipt(self, fuel_name: str, amount: float, liters: float):
        receipt = (
            f"\n----- Fuel Receipt -----\n"
            f"{self.__dispenser.formatted_date}\n"
            f"Fuel Type      : {fuel_name}\n"
            f"Amount Paid    : ₦{amount:.2f}\n"
            f"Liters Bought  : {liters:.2f} L\n"
            f"------------------------"
        )
        return receipt



    def get_available_fuel(self):
        return self.__dispenser.get_all_fuels()


    def get_all_transactions(self):
        transactions = []
        with open("transaction.txt", "r") as file:
            for history in file:
                transactions.append(history.strip())
        return transactions

