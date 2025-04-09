def compute_wage(hours_worked,rate):
    
    wage = hours_worked * rate
    
    return wage

def compute_allowance(wage,allowance_rate):
    
    allowance = wage * allowance_rate
    
    return allowance

def compute_gross_wage(allowance,wage):
    
    gross_wage = allowance + wage
    
    return gross_wage

def compute_tax(gross_wage,tax_rate):
    
    tax = gross_wage * tax_rate
    
    return tax

hours = int(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly rate: "))


wage = compute_wage(hours,rate)
allowance =compute_allowance(wage,0.1)
gross_wage = compute_gross_wage(allowance,wage)
tax = compute_tax(gross_wage,0.05)
   
print(wage)
print(allowance)
print(gross_wage)
print(tax)
     
       