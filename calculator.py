
# This calculator calculates profit and profit margin based on revenue and costs

#revenue and cost

revenue = float(input("Enter total revenue: $"))
costs = float(input("Enter total costs: $"))


# Calculate profits

profit = revenue-costs

# Calculate profit margin percentage

margin = (profit / revenue) * 100

# Display results

print("Company Finance")
print(f"Revenue: {revenue}$")
print(f"Costs: {costs}$")
print(f"Profit: {profit}$")
print(f"Profit Margin: {margin}%")