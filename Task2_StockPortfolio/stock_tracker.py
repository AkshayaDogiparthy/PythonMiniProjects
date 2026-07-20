import csv

prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "MICROSOFT": 320
}

portfolio_total = 0
portfolio_data = []

print("=== Stock Portfolio Calculator ===")

while True:
    company = input("Enter stock name (or exit to stop): ").upper()

    if company == "EXIT":
        break

    if company not in prices:
        print("Invalid stock name.")
        continue

    shares = int(input("Enter number of shares: "))

    investment = prices[company] * shares
    portfolio_total += investment

    portfolio_data.append([company, shares, investment])

print("\nPortfolio Details")
for item in portfolio_data:
    print(f"{item[0]} - {item[1]} shares = ${item[2]}")

print(f"\nTotal Portfolio Value: ${portfolio_total}")

with open("stock_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Company", "Shares", "Investment"])
    writer.writerows(portfolio_data)

print("Data saved in stock_data.csv")
