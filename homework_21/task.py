import json
from pathlib import Path
import traceback
from collections import Counter

base_dir = Path("Homework_21")
json_file = base_dir/("task.json")

try:
    with json_file.open("r") as file:
        data = json.load(file)
    
    class Employee:
         def __init__(self,name, position, salary):
             self.name = name
             self.position = position
             self.salary = float(salary) if salary and salary != "None" else 0
    class Department:
        def __init__(self,name,description,employees):
            self.name = name
            self.description = description
            self.employees = employees
            
        def get_salaries(self):
             return [emp.salary for emp in self.employees if emp.salary > 0]
        
        def calculate_average_salary(self):
            salaries = self.get_salaries()
            return sum(salaries) / len(salaries) if salaries else 0
            
            
        def calculate_max_salary(self):
            salaries = self.get_salaries()
            return max(salaries) if salaries else 0
        
        def calculate_min_salary(self):
           salaries = self.get_salaries()
           return min(salaries) if salaries else 0
        
        def count_positions(self):
            position_counter= Counter(emp.position for emp in self.employees)
            return dict(position_counter)
    
    departments = []
    for dept_data in data.values():
       employees = [Employee(emp["name"], emp["position"], emp["salary"]) for emp in dept_data["employees"]]
       department = Department(dept_data["name"],dept_data["description"],employees)
       departments.append(department)
  
    for dept in departments:
        print(f"Department : {dept.name}")
        print(f"Description : {dept.description}")
        print(f"Average Salary :{dept.calculate_average_salary()}")
        print(f"Max Salary :{dept.calculate_max_salary()}")
        print(f"Min Salary :{dept.calculate_min_salary()}")
        print(f"Position count :{dept.count_positions()}")
        print("-" * 25)
         
except FileNotFoundError as e:
    print(f"File not found {json_file}")
except json. JSONDecodeError as e:
    print(f"Error decoding JSON from the file: {json_file}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
    traceback.print_exc()
    