

"""
2. Შექმენით სამი სია და შეავსეთ შემთხვევითი რიცხვებით. 
Ეკრანზე დაბეჭდეთ ერთსა და იმავე ინდექსზე მდგარი 
რიცხვების ჯამები
"""
list_1 = [2,4,7,6]
list_2 = [2,5,6]
list_3 = [10,14,2]

result_of_finding_sum = list(map(lambda x, y, z : x + y + z, list_1, list_2, list_3))

def main ():
    print(result_of_finding_sum)
if __name__ == "__main__":
    main()