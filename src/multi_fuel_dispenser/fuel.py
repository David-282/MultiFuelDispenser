class Fuel:
    def __init__(self, fuel_name:str,price_per_liter:float,quantity:float):
        self.__fuel_name = None
        self.set_fuel_name (fuel_name)

        self.__price_per_liter = None
        self.set_price_per_liter (price_per_liter)

        self.__quantity = None
        self.set_quantity (quantity)

    def get_fuel_name(self):
        return self.__fuel_name

    def get_price_per_liter(self):
        return self.__price_per_liter

    def get_quantity(self):
        return self.__quantity

    def set_fuel_name(self,fuel_name:str):
        if fuel_name is None or fuel_name.strip() == "":
            raise ValueError("Fuel Name cannot be Empty")
        
        self.__fuel_name = fuel_name.lower()

    def set_price_per_liter(self,price_per_liter:float):
        if price_per_liter is None or price_per_liter <1:
            raise ValueError("Price per Liter cannot be zero")

        self.__price_per_liter = price_per_liter

    def set_quantity(self,quantity:float):
        if quantity is None or quantity < 1:
            raise ValueError("Quantity cannot be less than 1")

        self.__quantity = quantity