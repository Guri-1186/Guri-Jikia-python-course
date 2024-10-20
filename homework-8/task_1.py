"""
დაწერეთ პროგრამა რომელიც მიიღებს მიიღებს სტრიქონი და 
დაადგენს ეს ტექსტი არის თუ არა პალინდრომი.
Პალინდრომი არის სიტყვა რომელიც მარცხნიდან და მარჯვნიდან 
ერთნაირად იკითხება. Მაგალითად: radar, level, racecar არის პალინდრომები. 
Პროგრამამ უნდა დააიდენტიფიციროს პალინდრომი წინადადებაც. 
Წინადადებიდან უნდა უგულებელყოს ყველა სიმბოლო, 
გარდა ინგლისური სიმბოლოსებისა a-z, A-Z. Პროგრამამ უნდა უგულებელყოს 
სიმბოლოს რეგისტრი, 
Racecar არის პალინდრომი.
"""

while True:
    user_input = input("Please enter word:").lower()
    if user_input.replace(" ", "").isalpha():
   
        break
    else:
        print("please enter string")


output = ""        
for char in user_input:
    if char.isalpha():
      output+=char    
if output == output[::-1]:
        print("Is palindrome")
else:
        print ("Isn't palindrome")

    