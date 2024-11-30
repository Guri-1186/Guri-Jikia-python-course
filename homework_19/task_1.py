import json
from pathlib import Path
import traceback

base_dir = Path("homework_19")
json_file = base_dir/("stats.json")
final_file = base_dir/"avg_salary.json"
try:
    with json_file.open("r") as file:
        data = json.load(file)
    dict_salary = {}   
    for department, info in data.items():
        salaries = [float(emp["salary"])for emp in info["employees"] if emp["salary"] not in ["None",0]]
        avg_salary = sum(salaries) / len(salaries) if salaries else 0
        dict_salary[department] = avg_salary
    
    with final_file.open("w") as file:
        json.dump(dict_salary, file, indent=4)
    print(json.dumps(dict_salary, indent=4))
    
except FileNotFoundError as e:
    print(f" File not found {json_file}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON from the file: {json_file}")
except ValueError as e:
    print(f"value erros occurs {e}")
except Exception as ex:
       print(f"An unexpected error occurred: {ex}")
       traceback.print_exc()
    
   
            