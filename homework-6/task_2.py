"""
1.	დაწერეთ პროგრამა რომელიც მიიღებს დადებით მთელ რიცხვს - n. 0 < n <= 1000.
პროგრამამ უნდა დაბეჭდოს რიცხვების მიმდევრობა რომელიც მიიღება შემდეგი პირობით:
თუ რიცხვი ლუწია, ეს რიცხვი უნდა გავყოთ 2-ზე, 
ხოლო თუ რიცხვი კენტია ეს რიცხვი უნდა გავამრავლოთ 3-ზე და დავუმატოთ 1, 
იქამდე სანამ არ მივიღებთ 1-ს. Მაგალითი:
Enter number: 10
10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

ახსნა: 10 რადგან ლუწია გავყავით 2-ზე მივიღეთ 5
5 რადგან კენტია გავამრავლეთ 3-ზე და დავუმატეთ 1. მივიღეთ 16
ამის შემდეგ 16, 8, 4, 2 ლუწებია და ყველას ვყოფთ 2-ზე.
"""
positive_integer = int(input("Please enter positive integer with max value 1000 :"))
if positive_integer <= 0  or positive_integer > 1000:
    print("Invalid input")
    exit(1)
  
  
while positive_integer != 1:
    if positive_integer % 2 == 0:
        positive_integer //= 2
    elif positive_integer % 2 == 1:
         positive_integer = positive_integer * 3 + 1
    print(positive_integer, end = " ")
     
        

# while positive_integer != 1:
#     if positive_integer % 2 == 0:
#         positive_integer //= 2
#     elif positive_integer % 2 == 1:
#          positive_integer = positive_integer * 3 + 1
        
#     print(positive_integer, end = " ")
