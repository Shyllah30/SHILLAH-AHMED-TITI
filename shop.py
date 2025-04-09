cost_price = int(input("Enter cost price :"))

transport_cost = int(input(" Enter transport Cost :"))

selling_price = (cost_price + (5/100 * cost_price)) + (2/100 *transport_cost)

profit = selling_price - cost_price
print(profit)

if profit >0:
    print(f"Profit available")

else:
    print("Loss")

