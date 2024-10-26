""" 
6. Დაწერეთ ფუნქცია რომელსაც გადაეცემა მანქანის მწარმოებელი და გამოშვების წელი.
Მანქანის მწარმოებელი უნდა იყოს აუცილებელი არგუმენტი ხოლო გამოშვების წელის 
ნაგულისხმევი მნიშვნელობა უნდა იყოს მიმდინარე წელი. 
Ფუნქციას უნდა ჰქონდეს შესაძლებლობა, რომ გადაეცეს განუზღვრელი დასახელების
და რაოდენობის კონფიგურაციის პარამეტრები.
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ 
აჩვენოთ მისი მუშაობა
"""

def car_info(manufacturer, release_year = 2024, *args):
    print("manufacturer :", manufacturer)
    print("release_year :" , release_year)
  
    if args:
        print("additional info :")
        for additional_info in args:
            print("\t",additional_info)
   
car_info("mercedes")
car_info("BMW", 2023)
car_info("porshe", 2020, "white"," in the best condition", "hybrid")


    