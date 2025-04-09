#write a program to capture items taken, quantity of eachitem and price. The program should compute amount of each item and the total bill of all items

counter = 1
total_bill = 0
discount = 0
N0_of_item = 5

while True:

    item_taken = input("Enter item taken or Q  to stop : ")
    if item_taken.lower() == "q":
        break
    price = int(input("Enter price: "))
    quantity = int(input("Enter Quantity: "))
    amount = quantity * price
    print(amount)

    total_bill += amount
   
if total_bill >= 50000:
    discount = total_bill *0.1
net_amount = total_bill - discount

print(f" Total bill ={ total_bill}")



