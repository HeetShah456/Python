# Calculate net salary where net salary = gross salary + allowance - deduction. Allowances are 10% while deductions are 3% of gross salary.
gross_salary=float(input("Enter gross Salary : "))
allowance=10*gross_salary / 100
deduction=3*gross_salary / 100
net_salary=gross_salary+allowance-deduction
print("Net Salary : ",net_salary)