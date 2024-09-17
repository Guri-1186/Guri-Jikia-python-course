import random

"""
task-3 4. დაწერეთ პროგრამა რომელიც გაშვებისას დაბეჭდავს ბანქოს შემთხვევით 
მნიშვნელობას (სულ 52 შესაძლო მნიშვნელობა: 
4 ფერი (clubs (♣), diamonds (♦), hearts (♥) and spades (♠)) 
და 13 მნიშვნელობა (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2))
"""
suits = ['clubs (♣)', 'diamonds (♦)', 'hearts (♥)', 'spades (♠)']
values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

random_suits = random.choice(suits)
random_values = random.choice(values)
print(f"random cases of deck is: {random_suits} {random_values}")