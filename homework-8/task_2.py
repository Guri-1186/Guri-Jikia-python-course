
"""
2. დაწერეთ პროგრამა რომელიც მიიღებს ორ სტიქონს. 
Პროგრამამ უნდა შეამოწმოს არის თუ არა 
შესაძლებელი ერთი სტრიქოქნის სიმბოლოების გამოყენებით მეორე სტრიქონის მიღება.
"""
while True:
    input_1 = input ("Please enter first word :").lower()
    input_2 = input ("Please enter second word :").lower()
    if input_1.replace(" ", "").isalpha() and input_2.replace(" ", "").isalpha():
        break
    else:
        print("Please enter string ")

output = ""
for char in input_1:
   if char in input_2 and len(input_1) == len(input_2):
       if char.isalpha():
        output+=char

if output:
    print("Yes")
else:
    print("No")



    
     
