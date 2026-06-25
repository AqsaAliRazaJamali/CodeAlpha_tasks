stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}
stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))
if stock_name in stock_prices:
    investment = stock_prices[stock_name] * quantity
    print("Total investment value:", investment)
    with open("portfolio.txt","a") as file:
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Investment Value: {investment}\n")

    print("Result saved in portfolio.txt")
else:
    print("Stock not found")