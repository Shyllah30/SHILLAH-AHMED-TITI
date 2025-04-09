#a program  displaying the final bill

print("\t\tItems Available\t\t")

print("""
1. Burger\t 25000
2. Pizza\t  40000
3. Soda\t\t  5000
4. Coffee\t 8000
""")
item_taken = input("Enter Item Taken: ")


quantity =int(input("Enter Quantity: "))

item_code = int(input("Enter item code: "))

item_price = 0

if item_code == 1:
    if quantity >= 2:
     item_price = 25000 * quantity
     discount =(0.01 * item_price)
elif item_code == 2:
    item_price = 40000 * quantity
elif item_code == 3:
    item_price = 5000 * quantity
elif item_code == 4:
    item_price = 8000 * quantity
final_bill = item_price - discount    

print(f"item Price:{item_price}\nDiscount:{discount}\nFinal bill:{final_bill}")



