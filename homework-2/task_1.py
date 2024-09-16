
"""
task.1 Დაწერეთ პროგრამა რომელიც მიიღებს true ან false. 
Თუ პროგრამამ მიიღო true, ეკრანზე დაბეჭდეთ “whoala”.
"""
user_input = input("please enterter true or false :").lower()
if user_input == "true":
  print("whoala")
else:
  print("Its a wrong input")

 #OR
 
if user_input == "true":
  print("whoala")
elif user_input == "false":
  print("Its a false")
else:
  print("its a wrong input")
 
 