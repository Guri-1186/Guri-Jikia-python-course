"""
პროგრამამ უნდა შეგვაყვანინოს სიტყვა და დაბეჭდოს ამ 
სიტყვიდან მხოლოდ თანხმოვანი ასოები.
"""
while True:
    user_input = input("Please enter word :")
    if user_input.replace(" ", "").isalpha():
        break
    else:
        print("Please enter string")

for el in range(0, len(user_input)):
    if user_input[el].lower()  not in "aeiou":
        print(user_input[el])