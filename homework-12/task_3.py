import random
"""
დაწერეთ პროგრამა რომელიც დააგენერირებს 50 ცალ შემთხვევით
რიცხვს 1-დან 30-მდე და ჩაწერს სიაში. Პროგრამამ უნდა გადაუაროს სიას და 
მოაშოროს ყველა დუპლიკატი. 
დაბეჭდეთ ახალი სიის სიგრძე და თვითონ სია ეკრანზე
"""
list_1 = []
def random_numbers_generator():
    for _ in range(50): 
        random_num = random.randint(1, 30) 
        list_1.append(random_num)
    return list_1

def remove_dublicates():
    list_2 = []
    for el in list_1:
        if el not in list_2:
            list_2.extend([el])
    return list_2

def main():
    print(random_numbers_generator())
    new_list = remove_dublicates()
    print("List :", (new_list))
    print("length :", len((new_list)))
if __name__ == "__main__":
    main()   