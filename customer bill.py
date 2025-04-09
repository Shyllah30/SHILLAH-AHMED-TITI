#a program  displaying the final bill

print("\t\tItems Available\t\t")

print("""
1. Burger\t 25000
2. Pizza\t  40000
3. Soda\t   5000
4. Coffee\t 8000
""")
item_taken = input("Enter Item Taken: ")


quantity = input("Enter Quantity: ")

item_code = input("Enter item code: ")

item_price = 0

if item_code == 1:
    item_price = 25000 * quantity
elif quantity >= 2:
    discount = 0.01 * item_price






