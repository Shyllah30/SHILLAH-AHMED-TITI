# Aprogram to ask a user for the employee name, gender and hours worked.The programthen computes the wage as the product of hours worked and the fixed rate of 40000. Also computes allowances as 10% of wage, gross wage which is the summation of wage and allowance, tax is 5% of the gross an nrt wage is difference of gross and tax.The program should output the reqiured details

employee_name = input("what's your name :")

gender = input("what's your gender :")

hours_worked = input("How many hours have you worked? :")

fixed_rate = 40000

wage = int(hours_worked)*fixed_rate

allowance = 0.1 * wage

gross_wage = wage + allowance

tax = 0.05 * gross_wage

net_wage  = gross_wage - tax

print(f"wage = {wage}\nallowance = {allowance}\ngross_wage = {gross_wage}\ntax = {tax}\nnet_wage = {net_wage}")
