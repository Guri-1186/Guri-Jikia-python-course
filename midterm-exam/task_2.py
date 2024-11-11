"""
2. (8 ქულა) Დაწერეთ პროგრამა რომელიც მოხმარებელს მოსთხოვს შეიყვანოს 
მთელი რიცხვი n, სადაც 10 <= n <= 5432. 
Თუ მომხმარებელი შეიყვანს არასწორ რიცხვს ეკრანზე დაბეჭდეთ 
რომ პროგრამას გადმოეცა არასწორი რიცხვი და შეწყვიტეთ პროგრამის მუშაობა.
Თუ მომხმარებელი შეიყვანს სწორ რიცხვს, პროგრამამ უნდა იპოვოს ყველა 
13 ის ჯერადი რიცხვი 1-დან n-მდე.
Ეკრანზე დაბეჭდოს ეს რიცხვები და მათი საერთო რაოდენობა.
"""

def calc_num(num):
    result = []
    for i in range(1, num + 1):
        if i % 13 == 0:
            result.append(i)
    return result
         
def main():
    user_input = int(input("please enter number :"))
    if user_input <= 10 or user_input >= 432:
        print("Please enter valid number :")
        exit()
print(calc_num(13))

if __name__ == "__main__":
    main()
    
    