"""
პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა. დაბეჭდოს შეყვანილი სტრიქონის ყველა
ლუწი ინდექსის მქონე სიმბოლო, გარდა "e"- სიმბოლოსი. 
"""

user_input = input("Please enter string :")

for el in range(0,len(user_input)):
 if el % 2 == 0 and user_input[el] not in "e":
    print(user_input[el])
   
        