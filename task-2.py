prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330, "AMZN": 135}

portfolio = {}
print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(prices))
print("Type done when you are finished.")
print()

while True:
    name = input("Stock name: ").strip().upper()
    if name == "DONE":
        break
    if name not in prices:
        print("I don't have a price for that one.")
        print()
        continue
    qty = input("Quantity: ").strip()
    if not qty.isdigit() or int(qty) == 0:
        print("Enter a whole number bigger than 0.")
        print()
        continue
    qty = int(qty)
    if name in portfolio:
        portfolio[name] = portfolio[name] + qty
    else:
        portfolio[name] = qty
    print("Added", qty, "shares of", name)
    print()
if len(portfolio) == 0:
    print("You didn't add any stocks.")
else:
    total = 0
    print()
    print("Your portfolio:")
    for name in portfolio:
        value = portfolio[name] * prices[name]
        total = total + value
        print(name, "-", portfolio[name], "x", prices[name], "= $" + str(value))
    print("Total investment: $" + str(total))
    save = input("Save this to a file? (y/n): ").lower().strip()
    if save == "y":
        f = open("portfolio.txt", "w")
        f.write("Stock Portfolio\n\n")
        for name in portfolio:
            value = portfolio[name] * prices[name]
            f.write(name + " - " + str(portfolio[name]) + " shares = $" + str(value) + "\n")
        f.write("\nTotal: $" + str(total) + "\n")
        f.close()
        print("Saved to portfolio.txt")