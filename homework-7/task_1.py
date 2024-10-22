"""
პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა. დაბეჭდოს შეყვანილი სტრიქონის ყველა
ლუწი ინდექსის მქონე სიმბოლო, გარდა "e"- სიმბოლოსი. 
"""
while True:
    user_input = input("Please enter string :")
    if user_input.replace(" ", "").isalpha():
        break
    else:
        print(" Please enter only string")

for el in range(0, len(user_input)):
    if el % 2 == 0 and user_input[el].lower() not in "e":
        print(user_input[el])