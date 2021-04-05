employee_data = '{"employee_details":[{"employee_name": "James", "email": "james@gmail.com", "job_profile": "Sr. Developer"},{"employee_name": "Smith", "email": "Smith@gmail.com", "job_profile": "Project Lead"}]}'

import json

import csv

employee_parsed = json.loads(employee_data)
emp_data = employee_parsed['employee_details']
for data in emp_data:
    print(data)
# {'employee_name': 'James', 'email': 'james@gmail.com', 'job_profile': 'Sr. Developer'}
# {'employee_name': 'Smith', 'email': 'Smith@gmail.com', 'job_profile': 'Project Lead'}

with open('EmployData.csv', 'w') as employ_data:

    csvwriter = csv.writer(employ_data)
    csvwriter.writerow(["a", "b"])
    count = 0

    for emp in emp_data:

          if count == 0:

                 header = emp.keys()

                 csvwriter.writerow(header)

                 count += 1

          csvwriter.writerow(emp.values())

