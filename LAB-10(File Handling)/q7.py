import json
class Company:
    empcode = '24BCP308'
    empname = 'Shashvat Patel'
    DOJ = '18-04-2022'
    Salary = 150000
Employee = Company()

employee_data = {    
    "empcode": Employee.empcode,
    "empname": Employee.empname,
    "DOJ": Employee.DOJ,
    "Salary": Employee.Salary
}


f = open('ex.json','w+')
json.dump(employee_data,f)
f.seek(0)
obj = json.load(f)
print(obj)
