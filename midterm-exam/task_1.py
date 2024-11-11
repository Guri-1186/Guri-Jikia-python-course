"""
1. (5 ქულა) Დაწერეთ პროგრამა რომელიც
მომხმარებელს მოსთხოვს შეიყვანოს შემდეგი მონაცემები: 
სახელი, გვარი, ასაკი და ქალაქი. 
Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ 
ფორმატში: Hello სახელი გვარი. Age: ასაკი. City: ქალაქი.
"""

def personal_info (name, surname, age, city):
    print(f"Hello {name}, {surname} Age: {age} City:{city}")

def main():    
    personal_info("guri", "jikia", 30, "Tbilisi")
if __name__ == "__main__":
    main()
