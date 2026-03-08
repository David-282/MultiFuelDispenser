from multi_fuel_dispenser.dispenser import Dispenser
from multi_fuel_dispenser.fuel_attendant import FuelAttendant

# Initialize the Dispenser and FuelAttendant
dispenser = Dispenser()
print("OSHEY Filling Station, Yaba Branch")
print("======== Staff Login =========")
name = input("Hello Loyal Attendant, kindly enter your name: ")
fuel_attendant = FuelAttendant(name, dispenser)

while True:
    menu = """
Welcome to OSHEY Filling Station
1 -> Add A New Fuel
2 -> Sell Fuel By Amount
3 -> Sell Fuel By Liter
4 -> Restock Fuel
5 -> Update Fuel Price
6 -> Display All Fuel Products
7 -> Display All Transactions
0 -> Exit
"""
    print(menu)
    choice = input("Please enter your choice: ")

    match choice:
        case "1":
            fuel_name = input("Enter fuel name: ")
            try:
                price = float(input("Enter price per liter: "))
                quantity = float(input("Enter quantity in liters: "))
                fuel_attendant.add_new_fuel(fuel_name, price, quantity)
                print(f"{fuel_name} added successfully!")
            except ValueError:
                print("Invalid Input")

        case "2":
            fuel_name = input("Enter fuel name: ")
            try:
                amount = float(input("Enter amount to spend: "))
                receipt = fuel_attendant.sell_fuel_by_amount(fuel_name, amount)
                print(receipt)
            except ValueError:
                print("Invalid Input")

        case "3":
            fuel_name = input("Enter fuel name: ")
            try:
                liters = float(input("Enter liters to buy: "))
                receipt = fuel_attendant.sell_fuel_by_liter(fuel_name, liters)
                print(receipt)
            except ValueError:
                print("Invalid Input")

        case "4":
            fuel_name = input("Enter fuel name: ")
            try:
                liters = float(input("Enter liters to restock: "))
                fuel_attendant.restock_fuel(fuel_name, liters)
                print(f"{fuel_name} restocked successfully!")
            except ValueError:
                print("Invalid Input")

        case "5":
            fuel_name = input("Enter fuel name: ")
            try:
                new_price = float(input("Enter new price per liter: "))
                fuel_attendant.update_price(fuel_name, new_price)
                print(f"{fuel_name} price updated successfully!")
            except ValueError:
                print("Invalid Input")

        case "6":
            fuels = fuel_attendant.get_available_fuel()
            if len(fuels) == 0:
                print("No fuels available.")
            else:
                print("Available Fuel Products:")
                for fuel in fuels:
                    print(fuel)
                    # fuel_obj = dispenser.get_fuel(f)
                    # print(f"Fuel: {f}, Price: ₦{fuel_obj.get_price_per_liter:.2f}, Quantity: {fuel_obj.get_quantity():.2f} L")

        case "7":
            transactions = fuel_attendant.get_all_transactions()
            if not transactions:
                print("No transactions yet.")
            else:
                print("All Transactions:")
                for transaction in transactions:
                    print(transaction)

        case "0":
            print("Goodbye! Have a nice day.")
            break

        case _:
            print("Invalid choice. Please enter a number from 0 to 7.")

    # input("\nPress Enter to continue...")