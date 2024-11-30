import json
from pathlib import Path
import traceback
"""
TO DO :
1) Დაწერეთ პროგრამა რომელიც წაიკითხავს JSON ფაილს. - done

2)Პროგრამამ უნდა დაამუშავოს შეცდომა თუ ფაილი არ არსებობს და
დაბეჭდოს ეკრანზე ინფორმაციული შეტყობინება. done

3) Პროგრამამ ფაილში არსებული დეპარტამენტებისთვის უნდა დათვალოს თითოეული 
დეპარტამენტის საშუალო ხელფასი.

4) Უნდა დაამუშავოს პოტენციური შეცდომები. 

5) Დათვლილი საშუალოხელფასები უნდა დაბეჭდოს ეკრანზე და ჩაწეროს JSON ფაილში 
avg_salary.json.
"""

base_dir = Path("homework_19")
json_file = base_dir / "stats.json"
output_file = base_dir / "avg_salary.json"

try:
    with json_file.open("r") as file:
        data = json.load(file)
    avg_salaries = {}

    for department, value in data.items():
        print(f"Department: {department}")
        
        salaries = [float(emp["salary"]) for emp in value["employees"] if emp["salary"] not in ["None", 0]]
        
        if salaries: 
            average_salary = sum(salaries) / len(salaries)
            avg_salaries[department] = average_salary
        else:
            avg_salaries[department] = 0  
  
    print("Average salaries by department:")
    for department, salary in avg_salaries.items():
        print(f"{department}: {salary}")
        
    with output_file.open("w") as file:
        json.dump(avg_salaries, file, indent=4) 
    print(json.dumps(avg_salaries, indent = 4))
 
except FileNotFoundError as e:
    print(f" File not found {json_file}")
except json.JSONDecodeError as e :
     print(f"Error decoding JSON from the file: {json_file}")
except ValueError as e:
      print(f"There is Value error {e}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
    traceback.print_exc()
