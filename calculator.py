# Enhanced WoW Gold Calculator
def calculate_ah_profit(item_price, quantity):
    # WoW Auction House takes a 5% cut
    ah_cut = 0.05
    total_sale = item_price * quantity
    cut_amount = total_sale * ah_cut
    profit = total_sale - cut_amount
    return profit

def convert_to_currency(gold):
    # Convert gold to gold, silver, and copper
    total_copper = int(gold * 10000)  # Convert to copper (1g = 100s = 10000c)
    gold_amount = total_copper // 10000
    silver_amount = (total_copper % 10000) // 100
    copper_amount = total_copper % 100
    return gold_amount, silver_amount, copper_amount

def calculate_crafting_profit(sell_price, material_costs, quantity):
    # Calculate profit from crafting and selling an item
    total_sale = sell_price * quantity
    total_cost = material_costs * quantity
    profit = total_sale - total_cost
    return profit

# Track total gold across sessions
total_gold = 0

print("Welcome to the Enhanced WoW Gold Calculator!")
while True:
    print("\nOptions:")
    print("1. Calculate Auction House profit")
    print("2. Calculate crafting profit")
    print("3. View total gold earned")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        item_price = float(input("Enter the price per item (in gold): "))
        quantity = int(input("Enter the number of items to sell: "))
        profit = calculate_ah_profit(item_price, quantity)
        total_gold += profit
        g, s, c = convert_to_currency(profit)
        print(f"Profit after AH cut: {g}g {s}s {c}c")

    elif choice == "2":
        sell_price = float(input("Enter the selling price per crafted item (in gold): "))
        material_costs = float(input("Enter the total material cost per item (in gold): "))
        quantity = int(input("Enter the number of items to craft/sell: "))
        profit = calculate_crafting_profit(sell_price, material_costs, quantity)
        total_gold += profit
        g, s, c = convert_to_currency(profit)
        print(f"Crafting profit: {g}g {s}s {c}c")

    elif choice == "3":
        g, s, c = convert_to_currency(total_gold)
        print(f"Total gold earned: {g}g {s}s {c}c")

    elif choice == "4":
        print("Goodbye, adventurer!")
        break

    else:
        print("Invalid option, try again!")
