"""
3. Დაწერეთ პროგრამა რომელიც მიიღებს ინფორმაციას ვის ვინ დაუმეგობრდა. 
Თუ პროგრამამ მიიღო სიტყვა FINISH, უნდა დაასრულოს მუშაობა.
Თუ პროგრამამ მიიღო სიტყვა Giorgi – Nini, 
ნიშნავს რომ Nini დაუმეგობრდა Giorgi-ს და Giorgi დაუმეგობრდა Ninis. 
Პროგრამამ მუშაობის დასრულების წინ, ეკრანზე უნდა დაბეჭდოს ვინ ვისი მეგობარია. 
"""
def get_friends():
    friends = {} 
    while True:
        user_input = input("Enter names (e.g.'Giorgi - Nini') or 'FINISH': ").lower()
        if user_input == "finish":  
            break
        if " - " in user_input:
            name1, name2 = user_input.split(" - ")  
            friends[name1] = name2
            friends[name2] = name1
        else:
            print("Please use format: 'Name1 - Name2'")
    for person, friend in friends.items():
        print(f"{person} - {friend}")

get_friends()
