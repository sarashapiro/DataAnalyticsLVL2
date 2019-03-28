payroll=[{'ID': '001','Name': 'Mary','PayRate': 15,'Hours': 40},
		{'ID': '002','Name': 'John','PayRate': 22,'Hours': 25},
		{'ID': '003','Name': 'Bob','PayRate': 35,'Hours': 4},
		{'ID': '004','Name': 'Mel','PayRate': 43,'Hours': 62},
		{'ID': '005','Name': 'Jen','PayRate': 17,'Hours': 33},
		{'ID': '006','Name': 'Sue','PayRate': 29,'Hours': 45},
		{'ID': '007','Name': 'Ken','PayRate': 40,'Hours': 36},
		{'ID': '008','Name': 'Dave','PayRate': 20,'Hours': 17},
		{'ID': '009','Name': 'Beth','PayRate': 37,'Hours': 37},
		{'ID': '010','Name': 'Ray','PayRate': 16.50,'Hours': 80}

]

for employee in payroll:
if employee('Hours')>40:
		salary = (40*employee['PayRate'])+((employee['hours']-40)*1.5*employee['PayRate'])
else:
		salary = employee['hours']*employee['PayRate']
		
print("{0}:${1:.2f}".format(employee['Name'],salary))
