# Exemple de tables
employee_table = [
	{"Name": "John", "EmpId": 1, "DeptName": "IT"},
	{"Name": "Alice", "EmpId": 2, "DeptName": "HR"},
	# ... autres lignes de la table Employee
]

dept_table = [
	{"DeptName": "IT", "Manager": "Bob"},
	{"DeptName": "HR", "Manager": "Charlie"},
	# ... autres lignes de la table Dept
]

# Résultat final
result = []

# Boucle imbriquée pour la jointure
for employee_row in employee_table:
	for dept_row in dept_table:
    	if employee_row["DeptName"] == dept_row["DeptName"]:
        	# Construction du tuple et ajout au résultat
        	result_tuple = (employee_row["Name"], employee_row["EmpId"], employee_row["DeptName"], dept_row["Manager"])
        	result.append(result_tuple)

# Affichage du résultat
for row in result:
	print(row)
