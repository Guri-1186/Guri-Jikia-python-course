import random
"""
1. დაწერეთ პროგრამა რომელიც დააგენერირებს 100 შემთხვევით რიცხვს 10-დან 
1000000000-მდე. Პროგრამამ უნდა იპოვოს ყველაზე მოკლე რიცხვი მიმდევრობაში, 
ყველაზე გრძელი რიცხვი. 

Პროგრამამ უნდა დაალაგოს რიცხვები სიგრძის 
მიხედვით ზრდადობით, კლებადობით. Ყველა შედეგი დაბეჭდეთ ეკრანზე. 
Გამოიყენეთ min, max, sorted ფუნქციები
"""
my_list = [random.randint(10,1000000000) for _ in range(100)]
shortest_num = min(my_list, key = lambda x :len(str(x)))
longest_num = max(my_list, key = lambda x : len(str(x)))
sorted_ascending = sorted(my_list, key = lambda x: len(str(x)))
sorted_descending = sorted(my_list, key = lambda x: len(str(x)), reverse = True)

def main():
    print("Random list :", my_list)
    print("Shortest num :", shortest_num)
    print("longest num :", longest_num)
    print("Sorted ascending order :", sorted_ascending)
    print("Sorted descending order :", sorted_descending)

if __name__ == "__main__":
    main()