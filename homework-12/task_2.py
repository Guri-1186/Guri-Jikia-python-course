import random
"""
2. Დაწერეთ პროგრამა რომელიც დააგენერირებს 50 ცალ 
შემთხვევით რიცხვს 1-დან 30-მდე და ჩაწერს სიაში. 

Პროგრამამ უნდა გადაუაროს სიას და თითოეული ელემენტისთვის 
ეს ელემენტი ჩაწეროს ახალ სიაში, იმდენჯერ, რაც არის მისი მნიშვნელობა. 
დაბეჭდეთ ახალი სიის სიგრძე და თვითონ სია ეკრანზე
"""
list_1 = []
def random_numbers_generator():
    for _ in range(3): 
        random_num = random.randint(1, 3) 
        list_1.append(random_num)
    return list_1

def new_list_generator():
    new_list = []
    for num in list_1:
        new_list.extend([num] * num)
    return new_list
    
def main():
    print(random_numbers_generator())
    generated_list = new_list_generator()
    print("Length of new list :", len(generated_list))
    print("New list:", (generated_list))
if __name__ == "__main__":
    main()