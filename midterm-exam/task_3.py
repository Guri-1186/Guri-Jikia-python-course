import random
from random import choice

"""
3. (12 ქულა) Დაწერეთ თამაში rock, paper, scissor. 
Დაწერეთ ფუნქცია რომელიც დააგენერირებს შემთხვევითად 
ერთ-ერთ სიმბოლოს ჩამოთვლილი სამიდან R,P,S. 

Დაწერეთ მეორე ფუნქცია main, რომელშიც მომხმარებელს შეაყვანინებთ 
თავის არჩევანს R, P ან S. სიმარტივისთვის შეგიძლიათ უგულებელყოთ ყველა 
შემოწმება მომხმარებლის ინფუთზე.
Შეადარეთ ერთმანეთს მომხმარებლის
შემოყვანილი სიმბოლო და თქვენი ფუნქციის დაგენერირებული სიმბოლო და 
გამოავლინეთ გამარჯვებული. 
Წესები: R ამარცხებს S S ამარცხებს P P ამარცხებს R P P, R R, S S არის 
ფრე იმ შემთხვევაში თუ გვაქვს ფრე, 
უნდა მისცეთ კიდევ ერთი თამაშის საშუალება.

"""
import random
def generate_choice():
    return random.choice(['R', 'P', 'S'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == 'R' and computer_choice == 'S') or \
         (user_choice == 'S' and computer_choice == 'P') or \
         (user_choice == 'P' and computer_choice == 'R'):
        return "User"
    else:
        return "Computer"

def main():
    while True:
        user_choice = input("შეიყვანეთ R (Rock), P (Paper), ან S (Scissors): ").upper()
        if user_choice not in ['R', 'P', 'S']:
            print("არასწორი არჩევანი, სცადეთ კიდევ ერთხელ.")
            continue
        computer_choice = generate_choice()
        print(f"კომპიუტერის არჩევანი: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        if result == "Tie":
            print("ყაიმი! სცადეთ კიდევ ერთხელ.")
        elif result == "User":
            print("თქვენ გაიმარჯვეთ!")
            break
        else:
            print("კომპიუტერმა გაიმარჯვა!")
            break

if __name__ == "__main__":
    main()
