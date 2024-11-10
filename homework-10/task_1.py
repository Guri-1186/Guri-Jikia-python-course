"""
1. Დაწერეთ ფუნქცია რომელიც არგუმენტად მიიღებს ტექსტს და დაარუნებს ამ ტექსტში ხმოვნების რაოდენობას. 
Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
"""

def getvowel(text):
    output = ""
    for el in text:
        if el.lower() in "aeiou":
            output+=el
    
    return len(output)
        
print(getvowel("Tiko"))
print(getvowel("i love you"))
print(getvowel("You are lovely girl :))"))