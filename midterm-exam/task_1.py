"""
1. (5 ქულა) Დაწერეთ პროგრამა რომელიც
მომხმარებელს მოსთხოვს შეიყვანოს შემდეგი მონაცემები: 
სახელი, გვარი, ასაკი და ქალაქი. 
Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ 
ფორმატში: Hello სახელი გვარი. Age: ასაკი. City: ქალაქი.
"""

def personal_info(name, surname, age, city):
    print(f"Hello {name} {surname}.")
    print(f"Age: {age}.")
    print(f"City: {city}.")
def main():    
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    personal_info(name, surname, age, city)
if __name__ == "__main__":
    main()
