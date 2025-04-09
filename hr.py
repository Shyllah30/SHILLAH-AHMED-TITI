# A program to ask the user to enter employee name and hours worked the program should  display above average if the hours worked are 50 and above otherwise display below average and computes the wage at a rate of 30000 if the hours worked are 50 and above otherwise the rate is 25000

employee_name = input("Enter Employee Name :")

hours_worked = int(input("Enter Hours worked :"))

average_hours = 50
Above_rate = 30000
Below_rate = 25000

if hours_worked >= 50:
     print("Above average")
     wage = hours_worked * 30000

else:
    print("Below average")
    wage = hours_worked * 25000

print(wage)



