company = {(1, 308): 50000, (2, 268): 60000, (3, 290): 40000, (1, 261): 55000, (2, 245): 70000}
salary = {}

for (d, r), s in company.items():
    if d not in salary:
        salary[d] = {"total":s,"max": s, "min": s}  
    else:
        salary[d]["max"] = max(salary[d]["max"], s)
        salary[d]["min"] = min(salary[d]["min"], s)
        salary[d]["total"] += s 
    
print(salary)
